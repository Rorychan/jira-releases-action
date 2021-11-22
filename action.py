from jira import JIRA
import os

jira = JIRA(basic_auth=(os.getenv('JIRA_EMAIL'),os.getenv('JIRA_API_TOKEN')))

jira.create_version(name=os.getenv('JIRA_VERSION'), project=os.getenv('JIRA_PROJECT'), archived=False, released=True)
