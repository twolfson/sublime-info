from unittest import TestCase
from sublime_info import sublime_info


class TestRunFunction(TestCase):
    def test_run_exists(self):
        self.assertTrue(bool(sublime_info.run))
