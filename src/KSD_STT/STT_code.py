import time
import json
import os
try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)



# with open("private.json") as json_file:
with open(os.path.dirname(os.path.realpath(__file__)) + "/private.json") as json_file:
    json_data = json.load(json_file)

speech_key, service_region = json_data["speech_key"], json_data["service_region"]


def speech_recognize_async_from_file(weatherfilename):
    """performs one-shot speech recognition asynchronously with input from an audio file"""
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language = "ko-KR"
    audio_config = speechsdk.audio.AudioConfig(filename=weatherfilename)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result_future = speech_recognizer.recognize_once_async()

    result = result_future.get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))


def speech_recognize_continuous_from_file(weatherfilename):
    """performs continuous speech recognition with input from an audio file"""
    # <SpeechContinuousRecognitionWithFile>

    result_str = ""

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language = "ko-KR"
    audio_config = speechsdk.audio.AudioConfig(filename=weatherfilename)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    done = False

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        nonlocal done
        done = True

    def str_cpy(cpy):
        nonlocal result_str
        result_str += cpy

    #speech_recognizer.recognizing.connect(lambda evt: print('Recognizing: {}'.format(evt.result.text)))
    speech_recognizer.recognized.connect(lambda evt: str_cpy(evt.result.text))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)
    speech_recognizer.stop_continuous_recognition()

    print(result_str)
    return result_str


def speech_recognize_continuous_from_mic():

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language = "ko-KR"

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    done = False

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        nonlocal done
        done = True

    result_str = ""

    def str_cpy(cpy):
        nonlocal result_str
        result_str += cpy

    #speech_recognizer.recognizing.connect(lambda evt: print('Recognizing: {}'.format(evt.result.text)))
    speech_recognizer.recognized.connect(lambda evt: str_cpy(evt.result.text))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)
    speech_recognizer.stop_continuous_recognition()

    print(str_cpy)
    return str_cpy

class BinaryFileReaderCallback(speechsdk.audio.PullAudioInputStreamCallback):
    def __init__(self, filename: str):
        super().__init__()
        self._file_h = open(filename, "rb")

    def read(self, buffer: memoryview) -> int:
        try:
            size = buffer.nbytes
            frames = self._file_h.read(size)
            buffer[:len(frames)] = frames
            return len(frames)
        except Exception as ex:
            print('Exception in `read`: {}'.format(ex))
            raise

    def close(self) -> None:
        print('closing file')
        try:
            self._file_h.close()
        except Exception as ex:
            print('Exception in `close`: {}'.format(ex))
            raise


def compressed_stream_helper(compressed_format, weatherfilename):
    callback = BinaryFileReaderCallback(weatherfilename)
    stream = speechsdk.audio.PullAudioInputStream(stream_format=compressed_format, pull_stream_callback=callback)

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language = "ko-KR"

    audio_config = speechsdk.audio.AudioConfig(stream=stream)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    done = False

    result_str = ""

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        nonlocal done
        done = True

    def str_cpy(cpy):
        nonlocal result_str
        result_str += cpy

    #speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: str_cpy(evt.result.text))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)

    speech_recognizer.stop_continuous_recognition()

    print(result_str)
    return result_str


def pull_audio_input_stream_compressed_mp3(filename):
    compressed_format = speechsdk.audio.AudioStreamFormat(compressed_stream_format=speechsdk.AudioStreamContainerFormat.MP3)
    return compressed_stream_helper(compressed_format, filename)