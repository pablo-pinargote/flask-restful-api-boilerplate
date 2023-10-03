import json
import os

from __init__ import create_app

APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
APP_PORT = os.getenv('APP_PORT', 8080)

CONFIG_FILEPATH = os.environ.get('CONFIG_FILEPATH', 'settings/debug.json')

with open(CONFIG_FILEPATH) as config_file:
  settings = json.load(config_file)

api, containers = create_app({
  'id': settings.get('id', 'unset'),
  'name': settings.get('name', 'TBD'),
  'description': settings.get('description', 'TBD')
})

if __name__ == '__main__':
  api.run(host=APP_HOST, port=APP_PORT, debug='debug' in CONFIG_FILEPATH)
