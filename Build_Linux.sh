#!/bin/bash
docker run --rm -v "$(pwd):/src" cdrx/pyinstaller-linux:python3 \
    "pyinstaller --onefile --noconsole converter.py"