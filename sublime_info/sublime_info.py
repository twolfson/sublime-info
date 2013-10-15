# Load in core dependencies
import os

# Load in 3rd party dependencies
from shutilwhich import which


# Define a custom exception for when Sublime cannot be located
class SublimeTextNotFoundException(Exception):
    pass


class SublimeTextNotResolvedException(SublimeTextNotFoundException):
    pass


class SublimeTextNotAtLocationException(SublimeTextNotFoundException):
    pass


# Define internal lookup which ignores
def _get_sublime_path():
    # Attempt to resolve Sublime Text
    path = (which('subl') or
            which('sublime_text'))

    # If Sublime is not found, raise our exception
    if not path:
        raise SublimeTextNotResolvedException(
                'Sublime Text could not be found via the command "%s" or "%s"' %
                ('subl',
                 'sublime_text'))

    # Otherwise, return the path
    return path


def get_sublime_path():
    """Resolve Sublime Text path

    :raises SublimeTextNotFoundException: If Sublime Text cannot be found, an error will be raised
    :returns: If ``SUBLIME_TEXT_PATH`` is in OS environment, this will be returned.
              Otherwise, a ``which``-like resolution will be returned.
    :rtype: str
    """
    # TODO: environ
    sublime_path = os.environ.get('SUBLIME_TEXT_PATH', None)
    # If sublime_path is provided, verify it exists
    if sublime_path and not os.path.exists(sublime_path):
        raise SublimeTextNotAtLocationException(
                'Sublime Text could not be found at "%s"' % sublime_path)
    # Otherwise, use the internal lookup
    else:
        sublime_path = _get_sublime_path()

    # Return the found path
    return sublime_path
