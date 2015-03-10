#!/usr/bin/env python3

import platform
import random
import re
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


_RE_IS_UNICODE = re.compile('emoji/unicode/([0-9a-fA-F]+).png')

result = requests.get('https://api.github.com/emojis').json()

choice = random.choice(list(result))

uni_match = _RE_IS_UNICODE.search(result[choice])
if uni_match is not None:
    unicode_code_point = chr(int(uni_match.group(1), 16))
else:
    unicode_code_point = None

if unicode_code_point is not None:
    print(':{}: │ {}'.format(choice, unicode_code_point))
else:
    print(':{}:'.format(choice))

copy_to_clipboard(':{}:'.format(choice))
