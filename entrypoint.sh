#!/bin/sh -l
export JIRA_EMAIL=$1
export JIRA_API_TOKEN=$2
export JIRA_PROJECT=$3
export JIRA_VERSION=$4
export JIRA_SERVER=$5
export JIRA_RELEASED_STATUS=$6
python /app/action.py