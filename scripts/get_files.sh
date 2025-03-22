#!/bin/bash

TARGET_DIR="files"

NEW_FILES=$(git diff --name-only --diff-filter=M -- "$TARGET_DIR")
MODIFIED_FILES=$(git ls-files --others --exclude-standard -- "$TARGET_DIR")

echo $NEW_FILES
echo $MODIFIED_FILES

echo $NEW_FILES >> $GITHUB_ENV
echo $MODIFIED_FILES >> $GITHUB_ENV