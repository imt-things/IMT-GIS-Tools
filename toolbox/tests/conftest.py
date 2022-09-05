import pytest


class Messages:

    def addMessage(self, message):
        print(message)


@pytest.fixture
def messages():
    return Messages()


@pytest.fixture
def test_aprx_path():
    return "toolbox\\tests\\test_aprx\\Test_APRX.aprx"