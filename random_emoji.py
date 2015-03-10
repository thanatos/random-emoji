#!/usr/bin/env python3

import platform
import random
import subprocess

import requests


def copy_to_clipboard(text):
    if platform.system() == 'Linux':
        cmd = ['xsel', '-b']
    elif platform.system() == 'Darwin':
        cmd = ['pbcopy']
    else:
        return  # Don't know about this OS.
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    proc.communicate(text.encode('utf-8'))
    if proc.returncode != 0:
        raise RuntimeError('Failed to copy to clipboard.')


result = requests.get('https://api.github.com/emojis').json()

choice = random.choice(list(result.keys()))

print(':{}:'.format(choice))

copy_to_clipboard(':{}:'.format(choice))
