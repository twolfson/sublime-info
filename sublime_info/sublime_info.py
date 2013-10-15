# Load in core, 3rd party, and local dependencies
import os
from shutilwhich import which
from errors import STNotResolvedError, STBadLocationError


class SublimeInfo(object):
    # Load in an environment variable constant
    sublime_path=os.environ.get('SUBLIME_TEXT_PATH', None)

    # Define init
    def __init__(self, sublime_path=None):
        # Allow for customizaton of sublime_path
        if sublime_path:
            self.sublime_path = sublime_path

    # Define internal lookup which ignores
    @classmethod
    def _get_sublime_path(cls):
        # Attempt to resolve Sublime Text
        path = (which('subl') or
                which('sublime_text'))

        # If Sublime is not found, raise our exception
        if not path:
            raise STNotResolvedError(
                    'Sublime Text could not be found via the command "%s" or "%s"' %
                    ('subl',
                     'sublime_text'))

        # Otherwise, return the path
        return path


    @classmethod
    def get_sublime_path(cls):
        """Resolve Sublime Text path

        :raises STNotFoundError: If Sublime Text cannot be found, an error will be raised
        :returns: If ``SUBLIME_TEXT_PATH`` is in OS environment, this will be returned.
                  Otherwise, a ``which``-like resolution will be returned.
        :rtype: str
        """
        # If sublime_path is provided, verify it exists
        sublime_path = cls.sublime_path
        if sublime_path:
            if not os.path.exists(sublime_path):
                raise STBadLocationError(
                        'Sublime Text could not be found at "%s"' % sublime_path)
        # Otherwise, use the internal lookup
        else:
            sublime_path = cls._get_sublime_path()

        # Return the found path
        return sublime_path
