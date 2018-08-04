import json

class FileStorage(object):
    """Stores skills to a file"""
    def __init__(self, file_name):
        # TODO check that file exists
        self.file_name = file_name

    def list_skills(self):
        # TODO memoize?
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
