from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee

from tests import TESTS

def palindrome(code, runner=None):
    if "#" in code:
        return False, "'#' is not allowed."
    return code == code[::-1], "This is not a palindrome"

import sys

print(CheckiOReferee.__dict__)

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        inspector=palindrome).on_ready)
