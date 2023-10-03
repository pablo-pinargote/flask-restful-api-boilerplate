from http import HTTPStatus

from assertpy import assert_that

from src import create_app


class TestRequestingHomeEndpointShould:

  def test_fail_with_404_http_status_code(self, default_settings):
    api, container = create_app(default_settings)
    response = api.test_client().get('/')
    assert_that(response.status_code).is_equal_to(HTTPStatus.NOT_FOUND)
