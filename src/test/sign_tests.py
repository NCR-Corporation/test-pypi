#!/usr/bin/env python3

import datetime
import requests
import unittest.mock

from ..key import HmacKey
from ..sign import sign


class TestSign(unittest.TestCase):
    def test_get(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        headers = {
            "nep-organization": "test-org",
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT"
        }

        request = requests.Request('GET', 'https://api.ncr.com/test', headers=headers).prepare()
        signed = sign(request, key)

        self.assertEqual('AccessKey 4567cfac9cdbde12b271200afafc8b56:3dqAJuaAxVgyI0F2alaaTgjVOGBGAapxcvVbBg+imo94cT4lqdYJaIZwZ8EdW6Isc6WLRaIq4t4X+8w/opRTHA==', signed.headers['Authorization'])

    def test_post(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        body = {
            "userIds": [{
                "username": "acct:user@test-org"
            }]
        }

        headers = {
            "nep-organization": "test-org",
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT"
        }

        request = requests.Request('POST', 'https://api.ncr.com/test', json=body, headers=headers).prepare()
        signed = sign(request, key)

        self.assertEqual('TCDossuZJfZ4KDj8kaHhCA==', signed.headers['Content-MD5'])
        self.assertEqual('AccessKey 4567cfac9cdbde12b271200afafc8b56:m4n3zVQfiRpi7kpEmaA9q/yFeXItXgiizFm+tztU8uhI/jFG9yjxr5O4J8rSfYBof1u/pq7Ol4Np5FLM2GIEjw==', signed.headers['Authorization'])

    def test_post_no_body(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        headers = {
            "nep-organization": "test-org",
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT"
        }

        request = requests.Request('POST', 'https://api.ncr.com/test', headers=headers).prepare()
        signed = sign(request, key)

        self.assertEqual('AccessKey 4567cfac9cdbde12b271200afafc8b56:thadC5aoZgK16kM705ClannDbQJ5vWiV4k91Cw7qq3P4r5BLQfTmAxqDKN1SoHYRQtEG7eDuuP7i9v4n3xNXSg==', signed.headers['Authorization'])

    def test_post_content_type_required(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        body = 'hello'

        headers = {
            "nep-organization": "test-org",
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT"
        }

        request = requests.Request('POST', 'https://api.ncr.com/test', data=body, headers=headers).prepare()

        with self.assertRaises(Exception):
            signed = sign(request, key)

    def test_post_string_body(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        body = 'hello'

        headers = {
            "nep-organization": "test-org",
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT",
            "Content-Type": "application/text"
        }

        request = requests.Request('POST', 'https://api.ncr.com/test', data=body, headers=headers).prepare()
        signed = sign(request, key)

        self.assertEqual('XUFAKrxLKna5cZ2REBfFkg==', signed.headers['Content-MD5'])
        self.assertEqual('AccessKey 4567cfac9cdbde12b271200afafc8b56:K8QcPZRd/kQ6pmmaRgoI3tIQpryZeNza6o5SEbtlt3Qeb581pSQ5MTA+K8uT/HY7uAD48OeBkNS8jES4X9NROw==', signed.headers['Authorization'])

    def test_post_minimal(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        body = {
            "userIds": [{
                "username": "acct:user@test-org"
            }]
        }

        headers = {
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT"
        }

        request = requests.Request('POST', 'https://api.ncr.com/test', json=body, headers=headers).prepare()
        signed = sign(request, key)

        self.assertEqual('TCDossuZJfZ4KDj8kaHhCA==', signed.headers['Content-MD5'])
        self.assertEqual('AccessKey 4567cfac9cdbde12b271200afafc8b56:QKURoEUHMiE44b2JgDOkDGLUJGJC2u8Cc/5EOdzEmdz89Fxsw8Eubsrc75j3o2lkNTGPb96q1nzkTTdhtunaNg==', signed.headers['Authorization'])

    def test_post_application_key(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        body = {
            "userIds": [{
                "username": "acct:user@test-org"
            }]
        }

        headers = {
            "nep-application-key": "edd51013446a9cc339911c0bcce77da3",
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT"
        }

        request = requests.Request('POST', 'https://api.ncr.com/test', json=body, headers=headers).prepare()
        signed = sign(request, key)

        self.assertEqual('TCDossuZJfZ4KDj8kaHhCA==', signed.headers['Content-MD5'])
        self.assertEqual('AccessKey 4567cfac9cdbde12b271200afafc8b56:6N5Gqhd++bIpyx6lokRBcwchdcR0uz1LsmKSfis9GuRFA+pEwAAx0pZ50H1li3uZcWRCbbVAta5Q3DtiMh3ITw==', signed.headers['Authorization'])

    def test_post_correlation_id(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        body = {
            "userIds": [{
                "username": "acct:user@test-org"
            }]
        }

        headers = {
            "nep-correlation-id": "edd51013446a9cc339911c0bcce77da3",
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT"
        }

        request = requests.Request('POST', 'https://api.ncr.com/test', json=body, headers=headers).prepare()
        signed = sign(request, key)

        self.assertEqual('TCDossuZJfZ4KDj8kaHhCA==', signed.headers['Content-MD5'])
        self.assertEqual('AccessKey 4567cfac9cdbde12b271200afafc8b56:6N5Gqhd++bIpyx6lokRBcwchdcR0uz1LsmKSfis9GuRFA+pEwAAx0pZ50H1li3uZcWRCbbVAta5Q3DtiMh3ITw==', signed.headers['Authorization'])

    def test_post_service_version(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        body = {
            "userIds": [{
                "username": "acct:user@test-org"
            }]
        }

        headers = {
            "nep-service-version": "5.0",
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT"
        }

        request = requests.Request('POST', 'https://api.ncr.com/test', json=body, headers=headers).prepare()
        signed = sign(request, key)

        self.assertEqual('TCDossuZJfZ4KDj8kaHhCA==', signed.headers['Content-MD5'])
        self.assertEqual('AccessKey 4567cfac9cdbde12b271200afafc8b56:drD0MwZ6EGB9OqUIJ5BSkujs1go+Vf4tVE2RJYrL7iAImkfOnxlGAmmIc9gABP2EuUnM4xpu0nb7hEltsDn7GQ==', signed.headers['Authorization'])

    def test_post_all_headers(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        body = {
            "userIds": [{
                "username": "acct:user@test-org"
            }]
        }

        headers = {
            "nep-organization": "test-org",
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT",
            "nep-application-key": "edd51013446a9cc339911c0bcce77da3",
            "nep-correlation-id": "edd51013446a9cc339911c0bcce77da3",
            "nep-service-version": "5.0"
        }

        request = requests.Request('POST', 'https://api.ncr.com/test', json=body, headers=headers).prepare()
        signed = sign(request, key)

        self.assertEqual('TCDossuZJfZ4KDj8kaHhCA==', signed.headers['Content-MD5'])
        self.assertEqual('AccessKey 4567cfac9cdbde12b271200afafc8b56:JXqwD1HteQmhNQqYxgGSw35xvU72wneaEZAZulKTRYsmA8HzJrdvgk1IOa5no5cKFf6yHTgeS8C+t1EDb5PDPw==', signed.headers['Authorization'])

    def test_put(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        body = {
            "userIds": [{
                "username": "acct:user@test-org"
            }]
        }

        headers = {
            "nep-organization": "test-org",
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT"
        }

        request = requests.Request('PUT', 'https://api.ncr.com/test', json=body, headers=headers).prepare()
        signed = sign(request, key)

        self.assertEqual('TCDossuZJfZ4KDj8kaHhCA==', signed.headers['Content-MD5'])
        self.assertEqual('AccessKey 4567cfac9cdbde12b271200afafc8b56:1JcMGjVRGd03X7RX6/y7vXybQyZD89uAWUvNfeoV6kidsSvfKY/jC8tr8BPSISDbkLaFUFxZaXwyBTkeMUNOKg==', signed.headers['Authorization'])

    def test_delete(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        headers = {
            "nep-organization": "test-org",
            "Date": "Fri, 01 Jan 2021 12:30:23 GMT"
        }

        request = requests.Request('DELETE', 'https://api.ncr.com/test', headers=headers).prepare()
        signed = sign(request, key)

        self.assertEqual('AccessKey 4567cfac9cdbde12b271200afafc8b56:sCLQ0k5NK310f+BCOHkFL5zthMmi4XNrnlRwLXOJemNEfRkIVEsWyybdCN2yyw36PJguoZV6FglXzcP9WEXKlg==', signed.headers['Authorization'])

    def test_date_gen(self):
        key = HmacKey('d0d9ec3856b4697d36ec0389cf9e1b07', '4567cfac9cdbde12b271200afafc8b56')

        headers = {
            "nep-organization": "test-org"
        }

        request = requests.Request('GET', 'https://api.ncr.com/test', headers=headers).prepare()
        signed = sign(request, key)

        current_date = datetime.datetime.now(datetime.timezone.utc)
        generated_date = datetime.datetime.strptime(signed.headers['Date'], "%a, %d %b %Y %H:%M:%S %Z").replace(tzinfo=datetime.timezone.utc)

        self.assertLess((current_date - generated_date).total_seconds(), 5)
