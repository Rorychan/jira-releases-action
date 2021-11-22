#!/bin/bash
export JIRA_EMAIL=$1
export JIRA_API_TOKEN=$2
export JIRA_PROJECT=$3
export JIRA_VERSION=$4
python action.py