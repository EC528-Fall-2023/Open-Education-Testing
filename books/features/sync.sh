#!/bin/bash

git add -A

commit_message=$1
if [ -z "$commit_message" ]; then
    commit_message="Sync changes"
fi
git commit -m "$commit_message"

git push origin main
