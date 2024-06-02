#!/bin/bash

set -e

echo "Enter commit message:"
read commit_message

git add .

git commit -m "$commit_message"

git push

echo "Changes have been pushed successfully."
