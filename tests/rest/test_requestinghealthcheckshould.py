from http import HTTPStatus

from assertpy import assert_that

from src import create_app


class TestRequestingHealthCheckShould:

  def test_return_http_ok_status(self, default_settings):
    api, container = create_app(default_settings)
    response = api.test_client().get('/health-check')
    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)

  def test_return_app_id(self, default_settings):
    api, container = create_app(default_settings)
    response = api.test_client().get('/health-check')
    assert_that(response.json.get('welcome')).contains('my-id')

  def test_return_current_server_date_time(self, default_settings):
    api, container = create_app(default_settings)
    response = api.test_client().get('/health-check')
    assert_that(response.json).contains('theTime')
