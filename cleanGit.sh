#!/usr/bin/env bash

git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch $1" \
  --prune-empty --tag-name-filter cat -- --all
echo $1 >> .gitignore
git add .gitignore
git commit -m "$1 to .gitignore"
git push origin --force --all
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now