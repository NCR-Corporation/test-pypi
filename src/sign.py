#!/usr/bin/env python3

from __future__ import annotations

import hmac
import re

from base64 import b64encode
from datetime import datetime, timezone
from hashlib import md5, sha512
from requests import PreparedRequest

from .key import HmacKey


def sign(request: PreparedRequest, keys: HmacKey) -> PreparedRequest:
    content = []
    headers = {k.lower(): v for k, v in request.headers.items()}

    content.append(request.method.upper())
    content.append(re.sub('^https?://[^/]+', '', request.url))

    if request.body:
        if "content-type" not in headers:
            raise Exception("Content-Type header required when a body is present.")

        content.append(headers["content-type"])

        if isinstance(request.body, str):
            request.body = request.body.encode('utf-8')

        content_md5 = b64encode(md5(request.body).digest()).decode('utf-8')

        content.append(content_md5)
        request.headers["Content-MD5"] = content_md5

    if "nep-application-key" in headers:
        content.append(headers["nep-application-key"])

    if "nep-correlation-id" in headers:
        content.append(headers["nep-correlation-id"])

    if "nep-organization" in headers:
        content.append(headers["nep-organization"])

    if "nep-service-version" in headers:
        content.append(headers["nep-service-version"])

    content = [v for v in content if v is not None and v != '']
    content_str = "\n".join(content)

    if "date" not in headers:
        request.headers["Date"] = datetime.strftime(datetime.now(timezone.utc), "%a, %d %b %Y %H:%M:%S %Z").replace("UTC", "GMT")
        headers["date"] = request.headers["Date"]

    request_date = datetime.strptime(headers["date"], "%a, %d %b %Y %H:%M:%S %Z")
    special_signing_date = f"{request_date.isoformat().split('.')[0]}.000Z"
    key_bytes = f"{keys.secret_key}{special_signing_date}".encode('utf-8')
    content_bytes = content_str.encode('utf-8')

    digest_maker = hmac.new(key_bytes, content_bytes, sha512)
    digest = b64encode(digest_maker.digest()).decode('utf-8')

    request.headers["Authorization"] = f"AccessKey {keys.shared_key}:{digest}"

    return request
