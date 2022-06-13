# Author:   Lonnie Souder
# Date:     01/03/2022
# Contains information about commit messages

from enum import Enum, auto


class CommitType(Enum):
    fix = auto()
    feature = auto()
    breaking_change = auto()
    style = auto()

    @classmethod
    def parse(cls, str):
        for type in CommitType:
            if type.name == str:
                return type
        raise ValueError(f'{str} is not a valid CommitType')


class CommitMessage():
    '''Contains all relevant data for a commit message used to build a changelog'''

    def __init__(self, type, scope, description):
        self.type = type
        self.scope = scope
        self.description = description

    @classmethod
    def parse(cls, message):
        ''' Parses message'''
        message_pieces = list(map(lambda s: s.strip(), message.split(":")))
        num_pieces = len(message_pieces)
        scope = message_pieces[1] if num_pieces == 3 else None
        description = message_pieces[2] if num_pieces == 3 else message_pieces[1]
        return CommitMessage(
            CommitType.parse(message_pieces[0]),
            scope,
            description)
