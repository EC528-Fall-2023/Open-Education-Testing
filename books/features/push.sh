#!/bin/bash

commit_message=$1

if [ -z "$commit_message" ]; then
    commit_message=$(date "+%Y-%m-%d %H:%M:%S")
fi

git add .
git commit -m "$commit_message"
git push --force
