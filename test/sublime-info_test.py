# Load in dependencies
import os
from unittest import TestCase

# Load in local dependencies
from sublime_info import sublime_info

# Outline tests
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
            raises a STNotFoundError

TODO: What about sublime_text.exe
TODO: What about sublime_text.app
TODO: Create test.sh/cmd for OSX and Windows which do both EXPECT ERROR and not

TODO: Package dir
TODO: Build version
"""


# If we are in an error test
if os.environ.get('EXPECT_ERROR', None):
    class TestGetSublimePathError(TestCase):
        def test_get_sublime_path_raises(self):
            self.assertRaises(sublime_info.STNotFoundError,
                              sublime_info.get_sublime_path)

# Otherwise, run normal tests
else:
    class TestGetSublimePathNormal(TestCase):
        def test_get_sublime_path_finds_path(self):
            # Verify the path matches
            expected_path = os.environ['EXPECTED_PATH']
            actual_path = sublime_info.get_sublime_path()
            self.assertEqual(expected_path, actual_path)
