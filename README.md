# Simply create JIRA releases based on your github releases

###Example workflow:
```
name: ci
on:
  release:
    types: [published]
jobs:
  create-jira-release:
    runs-on: ubuntu-latest
    steps:
      - name: create release
        uses: Rorychan/jira-releases-action@v1
        with:
          jira-server: 'https://example.atlassian.com'
          jira-email: 'service-user@example.com'
          jira-api-token: ${{ secrets.JIRA_API_TOKEN }}
          project-name: 'EXA'
          release-name: ${{ github.event.release.name }}
```
###Prerequisities:
####This action should be run only on release github event.
You have to [create jira-service-user](https://community.atlassian.com/t5/Jira-Align-articles/Creating-a-Jira-Service-Account-with-Groups-and-Permission/ba-p/1605547) and [create API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) to be able to use JIRA API.


###Parameters description:

| Name | Description |
|----|----|
|**jira-server**|URL for you JIRA cloud server|
|**jira-email**|jira user email|
|**jira-api-token**|API token that you have created for your jira user|
|**project-name**|**KEY** of the JIRA project, do not use project name|
|**release-name**|Name that JIRA release will take, usually is a github release name|
|**is-released**|[Optional] Define should the release be in **"Released"**  status. Default is false|