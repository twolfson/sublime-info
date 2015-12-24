# Load in local modules for extension
from __future__ import absolute_import
from sublime_info.SublimeInfo import SublimeInfo
from sublime_info.errors import *

# Define sugar methods
def get_sublime_path():
    return SublimeInfo.get_sublime_path()


def get_sublime_version():
    return SublimeInfo.get_sublime_version()


def get_package_directory():
    return SublimeInfo.get_package_directory()
