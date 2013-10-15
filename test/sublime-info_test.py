# Load in dependencies
import os
from unittest import TestCase

# Load in local dependencies
import sublime_info

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
TODO: Installed package dir
TODO: Platform
TODO: Arch
"""


# If we are in an error test
if os.environ.get('EXPECT_ERROR', None):
    class TestGetSublimePathError(TestCase):
        def test_get_sublime_path_raises(self):
            """Assert that we raise an error when Sublime Text is not on disk."""
            self.assertRaises(sublime_info.STNotFoundError,
                              sublime_info.get_sublime_path)

# Otherwise, run normal tests
else:
    class TestGetSublimePathNormal(TestCase):
        def test_get_sublime_path_finds_path(self):
            """Assert that we find the proper path to Sublime Text."""
            expected_path = os.environ['EXPECTED_PATH']
            actual_path = sublime_info.get_sublime_path()
            self.assertEqual(expected_path, actual_path)

        def test_get_sublime_version_resolves_version(self):
            """Assert that we find the proper version of Sublime Text."""
            expected_version = int(os.environ['EXPECTED_VERSION'])
            actual_version = sublime_info.get_sublime_version()
            self.assertEqual(expected_version, actual_version)

        def test_get_sublime_version_locates_pkg_dir(self):
            """Assert that we find the proper package directory."""
            expected_pkg_dir = os.environ['EXPECTED_PKG_DIR']
            actual_pkg_dir = sublime_info.get_package_directory()
            self.assertEqual(expected_pkg_dir, actual_pkg_dir)
