# Load in core, 3rd party, and local dependencies
import os
import re
import subprocess
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
        """Resolve Sublime Text path (e.g. /usr/bin/subl)

        If ``SUBLIME_TEXT_PATH`` is provided via environment variables, it will be used.
        Otherwise, a ``which``-like resolution will be returned.

        :raises STNotFoundError: If Sublime Text cannot be found, an error will be raised.
        :returns: ``SUBLIME_TEXT_PATH`` or ``which``-like resolution
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

    @classmethod
    def get_sublime_version(cls):
        """Resolve Sublime Text version (e.g. 2221, 3047)

        Sublime Text is resolved via ``get_sublime_path``

        :raises Exception: If the Sublime Text version cannot be parsed, an error will be raised.
        :returns: Version of Sublime Text returned by ``sublime_text --version``.
        :rtype: int
        """
        # Get the path to sublime and grab the version
        sublime_path = cls.get_sublime_path()
        child = subprocess.Popen([sublime_path, '--version'], stdout=subprocess.PIPE)
        version_stdout = str(child.stdout.read())

        # Kill the child
        child.kill()

        # Parse out build number from stdout
        # Sublime Text 2 Build 2221
        # Sublime Text Build 3047
        version_match = re.search(r'\d{4}', version_stdout)
        if not version_match:
            raise Exception('Sublime Text version not found in "%s"' % version_stdout)

        # Coerce and return the version
        return int(version_match.group(0))

    @classmethod
    def get_package_directory(cls):
        """Resolve Sublime Text package directory (e.g. /home/todd/.config/sublime-text-2/Packages)

        :raises Exception: If the Sublime Text version is not recognized, an error will be raised.
        :returns: Path to Sublime Text's package directory
        :rtype: str
        """
        # TODO: On Windows, OSX these will not be the same
        # Get the version
        version = cls.get_sublime_version()

        # Run Linux-only logic for pkg_dir
        pkg_dir = None
        if version >= 2000 and version < 3000:
            pkg_dir = os.path.expanduser('~/.config/sublime-text-2/Packages')
        elif version >= 3000 and version < 4000:
            pkg_dir = os.path.expanduser('~/.config/sublime-text-3/Packages')

        # Assert the package dir was found
        if not pkg_dir:
            raise Exception('Sublime Text version "%s" not recognized' % version)

        # Return the package directory
        return pkg_dir
