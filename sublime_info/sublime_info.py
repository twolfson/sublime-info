# Load in dependencies
import shutilwhich
import shutil


# Define
def _get_sublime_path():
    print shutil.which('subl')


def get_sublime_path():
    """Resolve Sublime Text path

    :returns: If ``SUBLIME_TEXT_PATH`` is in OS environment, this will be returned.
              Otherwise, a ``which``-like resolution will be returned.
    :rtype: str
    """
    # TODO: environ
    return _get_sublime_path()
