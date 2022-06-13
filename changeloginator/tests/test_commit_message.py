# Author:   Lonnie Souder
# Date:     01/04/2022
# Unit tests for CommitMessage

import unittest
from changeloginator.commit_message import CommitMessage, CommitType


class TestCommitMessage(unittest.TestCase):

    def test_parse_commit_message(self):
        raw_message = (
            'fix: ABC-123: Caught Promise exception\n\n' +
            'We did not catch the promise exception thrown by the API call')
        commit_message = CommitMessage.parse(raw_message)
        self.assertEqual(commit_message.type, CommitType.fix)
        self.assertEqual(commit_message.scope, 'ABC-123')
        self.assertEqual(
            commit_message.description,
            ('Caught Promise exception\n\n' +
             'We did not catch the promise exception thrown by the API call'))

    def test_parse_commit_message_no_section(self):
        raw_message = (
            'breaking_change: Caught Promise exception\n\n' +
            'We did not catch the promise exception thrown by the API call')
        commit_message = CommitMessage.parse(raw_message)
        self.assertEqual(commit_message.type, CommitType.breaking_change)
        self.assertEqual(commit_message.scope, None)
        self.assertEqual(
            commit_message.description,
            ('Caught Promise exception\n\n' +
             'We did not catch the promise exception thrown by the API call'))

    def test_parse_commit_message_bad_message(self):
        with self.assertRaises(IndexError):
            CommitMessage.parse('this should break')

    def test_commit_type_parser(self):
        self.assertEqual(CommitType.fix, CommitType.parse('fix'))
        self.assertEqual(CommitType.feature,
                         CommitType.parse('feature'))
        self.assertEqual(CommitType.breaking_change,
                         CommitType.parse('breaking_change'))
        with self.assertRaises(ValueError):
            CommitType.parse('invalid-string')


if __name__ == '__main__':
    unittest.main()
