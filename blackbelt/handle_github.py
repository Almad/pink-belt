import os
import re
from subprocess import check_output
import sys

from github import Github
import json
import requests
import webbrowser

from config import config
from handle_trello import get_current_working_ticket, pause_ticket, comment_ticket

GITHUB_CLIENT_ID = "c9f51ce9cb320bf86f16"


def get_github_repo():
    return check_output(['git', 'config', '--get', 'remote.origin.url']).strip()


def get_remote_repo_info(github_repo_info):
    # 'git@github.com:apiaryio/apiary.git'
    match = re.match("^.*github.com\:(?P<owner>[a-zA-Z\_\-]+)\/{1}(?P<name>[a-zA-Z\-\_]+)\.git$", github_repo_info)
    if not match:
        raise ValueError("Cannot parse repo info. Bad remote?")
    return match.groupdict()


def pull_request():
    branch = get_current_branch()
    repo = get_github_repo()

    if 'github.com' not in repo:
        raise ValueError("Current git origin not on github.com; aborting")

    ticket = get_current_working_ticket()

    api = Github(config['github']['access_token'])

    pr_description = """

Pull request for [%(name)s](%(url)s).

    """ % ticket

    repo_info = get_remote_repo_info(repo)

    url = "https://api.github.com/repos/%(owner)s/%(name)s/pulls" % repo_info

    payload = {
        'title': ticket['name'],
        'base': 'master',
        'head': "%(owner)s:%(branch)s" % {'branch': branch, 'owner': repo_info['owner']},
        'body': pr_description
    }

    headers = {
        'Authorization': "token %s" % config['github']['access_token']
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    if r.status_code != 201:
        print r.json()
        raise ValueError("PR ended with status code %s: %s" % (r.status_code, r))

    pause_ticket(ticket)

    pr_info = r.json()

    ticket_comment = "Sending [pull request #%(number)s](%(html_url)s)" % pr_info

    comment_ticket(ticket, ticket_comment)

    print "Pull request %(pr_id)s for trello card %(ticket_url)s send!" % {
        'pr_id': pr_info['number'],
        'ticket_url': ticket['url']
    }

    webbrowser.open(pr_info['html_url'])


def get_current_branch():
    return check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip()
