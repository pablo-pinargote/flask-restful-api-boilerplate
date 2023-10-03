from http import HTTPStatus
from werkzeug.exceptions import HTTPException

from flask import Flask, Response

from rest.controllers import HomeController

from wiring import Container
from rest.core import ResourcesMapper


def create_app(app_meta):
  app = Flask(__name__)

  container = Container()
  container.init_resources()
  container.config.app_meta.from_value(app_meta)
  container.wire(packages=['rest'])

  app.container = container

  @app.errorhandler(Exception)
  def handle_exception(e):
    # Pass through HTTP errors
    if isinstance(e, HTTPException):
      return e
    # Non-HTTP exceptions are logged, but not passed through
    return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

  ResourcesMapper(app).register_actions(
    HomeController()
  )

  return app, container
