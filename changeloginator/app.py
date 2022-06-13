# Author:   Lonnie Souder
# Date:     01/03/2022
# Generates a changelog from git log with commits written in a specific format.

from changeloginator.commit_message import CommitType, CommitMessage

import git
import argparse
from pathlib import Path
from typing import List


def parse_commandline_args(args: str) -> argparse.Namespace:
    '''
    Parses commandline args
    Note: args should NOT include the program name (i.e. argv[0])
    '''
    parser = argparse.ArgumentParser(
        description='Generates a changelog for a git repository')
    parser.add_argument('repo', type=Path, help='Path to git repo')
    parser.add_argument('-o', '--output-file', type=Path,
                        default='changelog.md', help='File to write changelog to')
    return parser.parse_args(args)


def get_latest_tag_or_first_commit_on_current_branch(repo: git.Repo) -> git.Reference:
    if repo.tags:
        return sorted(
            repo.tags,
            key=lambda t: t.commit.committed_datetime,
            reverse=True)[0]
    else:
        return sorted(
            repo.iter_commits(repo.head),
            key=lambda c: c.committed_datetime)[0]


def get_commits_since(repo: git.Repo, start_commit: git.Reference) -> List[CommitMessage]:
    def try_parse(commit):
        try:
            return CommitMessage.parse(commit.message)
        except (ValueError, IndexError):
            print(
                f'SKIPPING Invalid commit message format for message: {commit.message}')
            return None
    commit_range_specifier = f'{repo.commit(start_commit)}..HEAD'
    commit_messages = map(try_parse, repo.iter_commits(commit_range_specifier))
    return list(filter(lambda x: x, commit_messages))


def list_commits_of_type(type: CommitType, commits: List[CommitMessage]) -> str:
    markdown = ''
    for commit in filter(lambda c: c.type == type, commits):
        markdown += (f'- {commit.description}\n')
    return markdown


def main(argv: str) -> int:
    args = parse_commandline_args(argv[1:])
    repo = git.Repo(args.repo)
    oldest_commit_of_interest = get_latest_tag_or_first_commit_on_current_branch(
        repo)
    commits = get_commits_since(repo, oldest_commit_of_interest)

    with open(args.output_file, 'w') as output_file:
        output_file.write('# Changelog  \n')
        output_file.write(
            f'{oldest_commit_of_interest} -- {repo.commit("HEAD")}  \n')
        output_file.write('## New Features:  \n')
        output_file.write(list_commits_of_type(CommitType.feature, commits))
        output_file.write('## Bugs Fixed:  \n')
        output_file.write(list_commits_of_type(CommitType.fix, commits))
    return 0
