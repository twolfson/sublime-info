from unittest import TestCase
from sublime_info import sublime_info


"""
# The majority of these will be satisfied via .travis.yml
Sublime Text as subl
    resolved via `get_sublime_path`
        has a path of `/usr/bin/subl`

Sublime Text as sublime_text
    resolved via `get_sublime_path`
        has a path of `/usr/bin/sublime_text`

Sublime Text as sublime_texttt
    specified via SUBLIME_TEXT_PATH
        resolved via `get_sublime_path`
            has a path of `/usr/bin/sublime_texttt`

sublime_info
    attempting to resolve Sublime Text
        when it does not exist
            raises a SublimeTextNotFoundException

TODO: What about sublime_text.exe
TODO: What about sublime_text.app

TODO: Package dir
TODO: Build version
"""


class TestGetSublimePath(TestCase):
    def test_get_sublime_path(self):
        # If we don't have Sublime installed, expect an error

        # Otherwise, verify the path matches
        # TODO: Realizing for OSX / Windows compat, we should let these be environment vars
        expected_cmd = os.environ.get('SUBLIME_TEXT_RENAME', 'subl')
        expected_path = '/usr/bin/expected_cmd' % expected_path
        path = sublime_info.get_sublime_path()
