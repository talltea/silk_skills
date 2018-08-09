import json
from dataclasses import dataclass
from typing import List

@dataclass
class SilkSkill:
    """a representation of a single skill"""
    name: str
    description: str
    prerequisites: List[str]
    aliases: List[str] = None
    level: str = 'Unknown'
    media: List[str] = None


class FileStorage(object):
    """Stores skills to a file"""
    def __init__(self, file_name):
        # TODO check that file exists
        self.file_name = file_name

    def list_skills(self):
        # TODO memoize?
        # TODO handle malformed input
        with open(self.file_name) as f:
            data = json.load(f)
        if data is None:
            data = []
        return data

    def _overwrite_skills(self, skills):
        with open(self.file_name, 'w') as f:
            json.dump(skills, f)

    def add_skill(self, skill):
        skills = self.list_skills()
        skills.append(skill)
        self._overwrite_skills(skills)
