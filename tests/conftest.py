import pyramid.testing
import pytest

@pytest.yield_fixture
def config():
    config = pyramid.testing.setUp(settings={'retry.attempts': 3})
    config.include('pyramid_retry')
    yield config
    pyramid.testing.tearDown()
