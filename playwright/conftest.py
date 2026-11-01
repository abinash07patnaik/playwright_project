import pytest
from requests import session


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param