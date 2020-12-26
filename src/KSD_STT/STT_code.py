#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
"""
Speech recognition samples for the Microsoft Cognitive Services Speech SDK
"""

import time

try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError as e:
    print(e)
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)


# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "3821b1589d544d8e88be297d871854c5", "koreacentral"

# Specify the path to an audio file containing speech (mono WAV / PCM with a sampling rate of 16
# kHz).

# weatherfilename = "data/consulting02.wav"음성데이터/공공스포츠클럽_인터뷰_태권도.wav
weatherfilename = "voice_data/공공스포츠클럽_인터뷰_태권도.wav"

def speech_recognize_async_from_file(audio_file):
    """performs one-shot speech recognition asynchronously with input from an audio file"""
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language = "ko-KR"
    audio_config = speechsdk.audio.AudioConfig(filename=weatherfilename)
    # Creates a speech recognizer using a file as audio input.
    # The default language is "en-us".
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Perform recognition. `recognize_async` does not block until recognition is complete,
    # so other tasks can be performed while recognition is running.
    # However, recognition stops when the first utterance has bee recognized.
    # For long-running recognition, use continuous recognitions instead.
    result_future = speech_recognizer.recognize_once_async()

    print('recognition is running....')
    # Other tasks can be performed here...

    # Retrieve the recognition result. This blocks until recognition is complete.
    result = result_future.get()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))


def speech_recognize_continuous_from_file(file_name):
    """performs continuous speech recognition with input from an audio file"""
    # <SpeechContinuousRecognitionWithFile>
    #resultFile = open("result.txt", "w")

    result_str = ""

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language = "ko-KR"
    # audio_config = speechsdk.audio.AudioConfig(filename=weatherfilename)
    audio_config = speechsdk.audio.AudioConfig(filename=file_name)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    #speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    done = False

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        nonlocal done
        done = True

    def str_cpy(cpy):
        nonlocal result_str
        result_str += cpy
    # Connect callbacks to the events fired by the speech recognizer
    #speech_recognizer.recognizing.connect(lambda evt: print('Recognizing: {}'.format(evt.result.text)))
    # speech_recognizer.recognized.connect(lambda evt: print('Recognized: {}'.format(evt.result.text)))
    speech_recognizer.recognized.connect(lambda evt: str_cpy(evt.result.text))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)
    #resultFile.close()
    speech_recognizer.stop_continuous_recognition()

    print(result_str)
    return result_str
    # </SpeechContinuousRecognitionWithFile>
