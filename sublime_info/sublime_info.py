# Load in dependencies
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
    # TODO: If environ exists, still use os.path.exists
    return _get_sublime_path()
