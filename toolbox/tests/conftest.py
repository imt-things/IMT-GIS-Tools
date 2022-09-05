import pytest


class Messages:

    def addMessage(self, message):
        print(message)


@pytest.fixture
def messages():
    return Messages()