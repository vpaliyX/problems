#! usr/bin/bash
# Created By Vasyl Paliy
# 2017

echo "Enter the message for the commit:"
read message
git add .
git commit -m "$message"
git push origin master
