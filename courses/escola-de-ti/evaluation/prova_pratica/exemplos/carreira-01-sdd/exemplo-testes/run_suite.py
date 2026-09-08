"""Espera a API do app ficar disponível e roda a suíte do professor."""

import os
import sys
import time

import requests

url = os.environ.get("APP_URL", "http://localhost:8000").rstrip("/") + "/courts"

for _ in range(30):
    try:
        if requests.get(url, timeout=2).status_code < 500:
            break
    except requests.RequestException:
        pass
    time.sleep(2)
else:
    print("API do app não respondeu em 60s", file=sys.stderr)
    sys.exit(1)

import pytest

sys.exit(pytest.main(["suite_professor.py", "-v"]))
