#!/usr/bin/env python3

from random import randrange


def generate_key():
    out = ''

    for i in range(16):
        out += f'{randrange(0, 256):02x}'

    return out
