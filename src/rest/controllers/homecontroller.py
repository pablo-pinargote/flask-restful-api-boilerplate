import datetime

from http import HTTPStatus

from dependency_injector.wiring import Provide

from rest.core.decorators import get
from wiring import Container


class HomeController:

  @get('/health-check')
  def health_check(self, app_meta: dict = Provide[Container.config.app_meta]):
    """
    ---
    get:
      description: Health check endpoint.
      parameters: []
      responses:
        '200':
          description: OK
    """

    return {'Hi': 'stranger',
            'welcome': f'to the {app_meta.get("id", "no-id-set-yet")}',
            'I': 'am healthy :) !',
            'theTime': datetime.datetime.utcnow()
            }, HTTPStatus.OK
