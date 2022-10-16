# conftest.py

import os
import pytest

@pytest.fixture
def slug():
	return os.getenv('ATALERT_TEST_SLUG')

