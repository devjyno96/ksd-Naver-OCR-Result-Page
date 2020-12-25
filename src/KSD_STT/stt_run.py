#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

# import samples.python.console.speech_sample as speech_sample
from . import STT_code as speech_sample

from collections import OrderedDict
import platform

eofkey = 'Ctrl-Z' if "Windows" == platform.system() else 'Ctrl-D'

samples = OrderedDict([
    (speech_sample, [
        speech_sample.speech_recognize_async_from_file,
        speech_sample.speech_recognize_continuous_from_file,
    ])
])


def run(file_name):
    modules = list(samples.keys())
    result_str = ''
    try:
        selected_module = modules[0]
    except EOFError:
        raise
    except Exception as e:
        print(e)
        return

    try:
        num = 1 #int(input())
        selected_function = samples[selected_module][num]
    except EOFError:
        raise
    except Exception as e:
        print(e)
        return

    print('You selected: {}'.format(selected_function.__name__))
    try:
        result_str = selected_function(file_name)
    except Exception as e:
        print('Error running sample: {}'.format(e))

    return result_str
