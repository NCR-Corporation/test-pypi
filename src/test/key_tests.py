#!/usr/bin/env python3

import unittest

from ..key import HmacKey
from .test_utils import generate_key


class TestHmacKey(unittest.TestCase):
    def test_default(self):
        key = HmacKey()

        self.assertIsNone(key.secret_key)
        self.assertIsNone(key.shared_key)

    def test_positional(self):
        shared_key = generate_key()
        secret_key = generate_key()

        key = HmacKey(secret_key, shared_key)

        self.assertEqual(shared_key, key.shared_key)
        self.assertEqual(secret_key, key.secret_key)

    def test_explicit(self):
        shared_key = generate_key()
        secret_key = generate_key()

        key = HmacKey(secret_key=secret_key, shared_key=shared_key)

        self.assertEqual(shared_key, key.shared_key)
        self.assertEqual(secret_key, key.secret_key)

    def test_set(self):
        shared_key = generate_key()
        secret_key = generate_key()

        key = HmacKey()
        key.secret_key = secret_key
        key.shared_key = shared_key

        self.assertEqual(shared_key, key.shared_key)
        self.assertEqual(secret_key, key.secret_key)

