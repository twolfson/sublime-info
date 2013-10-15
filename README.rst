sublime-info
============

.. image:: https://travis-ci.org/twolfson/sublime-info.png?branch=master
   :target: https://travis-ci.org/twolfson/sublime-info
   :alt: Build Status

Gather information about `Sublime Text`_

This was built for the `Sublime plugin tests`_ framework. It provides a cross-platform way to collect data about `Sublime Text`_ without running `Sublime Text`_ (necessary for creating a plugin harness to `Sublime Text`_).

.. _`Sublime Text`: http://sublimetext.com/
.. _`Sublime plugin tests`: https://github.com/twolfson/sublime-plugin-tests

..
    Currently, only Linux is supported but OSX and Windows support are planned.

Getting Started
---------------
Install the module with: ``pip install sublime_info``

.. code:: python

    import sublime_info
    sublime_info.get_sublime_path()  # /usr/bin/subl
    sublime_info.get_sublime_version()  # 3047
    sublime_info.get_package_directory()  # /home/todd/.config/sublime-text-2/Packages

Documentation
-------------
`sublime_info` provides 3 top level functions for your consumption.

get_sublime_path
^^^^^^^^^^^^^^^^
.. code:: python
    get_sublime_path()  # /usr/bin/subl
    """Resolve Sublime Text path (e.g. /usr/bin/subl)

    If ``SUBLIME_TEXT_PATH`` is provided via environment variables, it will be used.
    Otherwise, a ``which``-like resolution will be returned.

    :raises STNotFoundError: If Sublime Text cannot be found, an error will be raised.
    :returns: ``SUBLIME_TEXT_PATH`` or ``which``-like resolution
    :rtype: str
    """

Contributing
------------
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Test via ``nosetests``.

Donating
--------
Support this project and `others by twolfson`_ via `gittip`_.

.. image:: https://rawgithub.com/twolfson/gittip-badge/master/dist/gittip.png
   :target: `gittip`_
   :alt: Support via Gittip

.. _`others by twolfson`:
.. _gittip: https://www.gittip.com/twolfson/

Unlicense
---------
As of Oct 14 2013, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the `UNLICENSE`_.

.. _UNLICENSE: https://github.com/twolfson/sublime-info/blob/master/UNLICENSE
