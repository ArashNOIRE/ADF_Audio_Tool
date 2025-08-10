#!/bin/bash
docker run --rm -v "$(pwd):/src" cdrx/pyinstaller-windows:python3 \
    "pyinstaller --onefile --noconsole converter.py"