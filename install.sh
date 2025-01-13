#!/bin/bash

# ensure current repository is root
cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

# ensure poetry is installed
if ! command -v poetry &>/dev/null; then
  curl -sSL https://install.python-poetry.org | python3 - --yes
fi

EXTRA_FLAGS=""
for extra in "$@"; do
  EXTRA_FLAGS="$EXTRA_FLAGS -E $extra"
done

poetry install $EXTRA_FLAGS
