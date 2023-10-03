import json

import pytest


@pytest.fixture
def default_settings():
  with open('settings/default.json') as settings_as_json:
    return json.load(settings_as_json)
