from jira import JIRA
import os

jira = JIRA(server=os.getenv('JIRA_SERVER'),basic_auth=(os.getenv('JIRA_EMAIL'),os.getenv('JIRA_API_TOKEN')))

jira.create_version(name=os.getenv('JIRA_VERSION'), project=os.getenv('JIRA_PROJECT'), archived=False, released=True)
