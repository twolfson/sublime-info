#!/bin/sh

# If there is a Sublime Text version, then install Sublime
if test -n "$SUBLIME_TEXT_VERSION"; then
  curl http://rawgithub.com/twolfson/sublime-installer/0.1.1/install.sh | sh -s $SUBLIME_TEXT_VERSION

  # If there is a rename, rename subl
  if test -n "$SUBLIME_TEXT_RENAME"; then
    sudo mv /usr/bin/subl /usr/bin/$SUBLIME_TEXT_RENAME
  fi
fi