#! /usr/bin/env bash
set -e

python /app/src/tests_pre_start.py

bash ./scripts/test.sh "$@"
