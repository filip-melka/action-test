#!/bin/bash

TARGET_DIR="files"

NEW_FILES=$(git diff --name-status HEAD~1 HEAD | awk '$1=="A" && $2 ~ /\.md$/ {print $2}')
MODIFIED_FILES=$(git diff --name-status HEAD~1 HEAD | awk '$1=="M" && $2 ~ /\.md$/ {print $2}')

echo "New files:"
echo "$NEW_FILES"
echo "Modified files:"
echo "$MODIFIED_FILES"

echo "NEW_FILES<<EOF" >> $GITHUB_ENV
echo "$NEW_FILES" >> $GITHUB_ENV
echo "EOF" >> $GITHUB_ENV

echo "MODIFIED_FILES<<EOF" >> $GITHUB_ENV
echo "$MODIFIED_FILES" >> $GITHUB_ENV
echo "EOF" >> $GITHUB_ENV