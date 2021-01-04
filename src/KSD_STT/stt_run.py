#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

# import samples.python.console.speech_sample as speech_sample
from . import STT_code as speech_sample

import platform
from pathlib import Path

eofkey = 'Ctrl-Z' if "Windows" == platform.system() else 'Ctrl-D'


def run(bool_mic: bool, file_name: str):
    print(file_name)
    if bool_mic:
        result = speech_sample.speech_recognize_continuous_from_mic()
    else:
        ext = Path(file_name).suffix
        if ext == ".wav":
            result = speech_sample.speech_recognize_continuous_from_file(file_name)
        elif ext == ".mp3":
            result = speech_sample.pull_audio_input_stream_compressed_mp3(file_name)
        else:
            result = "not supported file extension"
    return result