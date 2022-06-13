# Author:   Lonnie Souder
# Date:     01/07/2022
# Test for app


import unittest
from changeloginator import app
from changeloginator.commit_message import CommitMessage, CommitType
from argparse import Namespace
from pathlib import Path


class TestApp(unittest.TestCase):

    def test_parse_command_line_args(self):
        self.assertEqual(app.parse_commandline_args(['/some/dir']),
                         Namespace(repo=Path('/some/dir'), output_file=Path('changelog.md')))
        self.assertEqual(app.parse_commandline_args(['/some/dir', '-o' 'output.md']),
                         Namespace(repo=Path('/some/dir'), output_file=Path('output.md')))
        with self.assertRaises(SystemExit):
            app.parse_commandline_args([])

    def test_list_commits_of_type(self):
        commits = [CommitMessage(CommitType.fix, '', 'description1'),
                   CommitMessage(CommitType.fix, 'some-scope', 'description2'),
                   CommitMessage(CommitType.feature, '', 'description3'),
                   CommitMessage(CommitType.feature,
                                 'some-scope', 'description4'),
                   CommitMessage(CommitType.style, '', 'description5'),
                   CommitMessage(CommitType.breaking_change, '', 'description6')]
        self.assertEqual(app.list_commits_of_type(CommitType.fix, commits),
                         '- description1\n- description2\n')
        self.assertEqual(app.list_commits_of_type(CommitType.feature, commits),
                         '- description3\n- description4\n')


if __name__ == '__main__':
    unittest.main()
