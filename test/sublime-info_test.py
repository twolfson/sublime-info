from unittest import TestCase
from sublime_info import run

class TestRunFunction(TestCase):
    def run_exists(self):
        self.assertTrue(run)
