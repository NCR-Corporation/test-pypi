#!/usr/bin/env python3

from __future__ import annotations

from typing import Optional


class HmacKey:
    @property
    def secret_key(self) -> Optional[str]:
        return self._secret_key

    @secret_key.setter
    def secret_key(self, value: Optional[str]):
        self._secret_key = value

    @property
    def shared_key(self) -> Optional[str]:
        return self._shared_key

    @shared_key.setter
    def shared_key(self, value: Optional[str]):
        self._shared_key = value

    def __init__(self, secret_key: Optional[str] = None, shared_key: Optional[str] = None):
        self._secret_key = secret_key
        self._shared_key = shared_key
