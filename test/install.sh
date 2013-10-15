#!/bin/sh

# If there is a Sublime Text version, then install Sublime
if test -n "$SUBLIME_TEXT_VERSION"; then
  # Use script for ease of use
  curl http://rawgithub.com/twolfson/sublime-installer/0.1.1/install.sh | sh -s $SUBLIME_TEXT_VERSION

  # Output Sublime version
  subl --version

  # By default, expect this path
  EXPECTED_PATH="/usr/bin/subl"

  # If there is a rename, rename subl and update the expected path
  if test -n "$SUBLIME_TEXT_RENAME"; then
    sudo mv /usr/bin/subl /usr/bin/$SUBLIME_TEXT_RENAME
    EXPECTED_PATH="/usr/bin/$SUBLIME_TEXT_RENAME"
  fi
else
# Otherwise, expect an error
  EXPECT_ERROR="1"
fi