#!/bin/bash -e

# ensure current repository is root
cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

# ensure poetry is installed
if ! command -v poetry &>/dev/null; then
  curl -sSL https://install.python-poetry.org | python3 - --yes
fi

ENVIRONMENT="${1:-PROD}"

ENVIRONMENT="$(echo $ENVIRONMENT | tr '[:upper:]' '[:lower:]')"

case "$ENVIRONMENT" in
  production|prod)
    poetry install
    ;;
  development|dev)
    poetry install --with lint,test
    poetry run pre-commit install
    ;;
  *)
    echo "Unknown environment: $ENVIRONMENT."
    exit 1
    ;;
esac
