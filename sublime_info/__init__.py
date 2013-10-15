# Load in local modules for extension
from sublime_info import SublimeInfo
from errors import *

# Define sugar methods
def get_sublime_path():
    return SublimeInfo.get_sublime_path()


def get_sublime_version():
    return SublimeInfo.get_sublime_version()


def get_package_directory():
    return SublimeInfo.get_package_directory()
