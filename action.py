from jira import JIRA
import os

jira = JIRA(server=os.getenv('JIRA_SERVER'),basic_auth=(os.getenv('JIRA_EMAIL'),os.getenv('JIRA_API_TOKEN')))
is_released = os.getenv('JIRA_RELEASED_STATUS')
if is_released == 'true':
    jira.create_version(name=os.getenv('JIRA_VERSION'), project=os.getenv('JIRA_PROJECT'), archived=False, released=True)
else:
    jira.create_version(name=os.getenv('JIRA_VERSION'), project=os.getenv('JIRA_PROJECT'), archived=False, released=False)