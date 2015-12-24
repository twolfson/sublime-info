#!/usr/bin/env bash
# Exit on first error
set -e

# Run our tests
nosetests --nocapture
