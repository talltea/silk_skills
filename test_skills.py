import json
import mock
import pytest
import unittest
from skill_storage import FileStorage


TEST_FILE_NAME = 'test_file.json'

TEST_SINGLE_SKILL = {"test_skill": "yup, that's me"}

TEST_FILE_CONTENTS = [
    {"test": 55},
    {"I'm new!": "hi"}
]


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage(TEST_FILE_NAME)

    @mock.patch(
        'skill_storage.open',
        new_callable=mock.mock_open,
        read_data=json.dumps(TEST_FILE_CONTENTS),
    )
    def test_list(self, open_mock):
        results = self.storage.list_skills()
        assert(results == TEST_FILE_CONTENTS)

    @pytest.mark.skip(reason="failing to mock empty file")
    @mock.patch(
        'skill_storage.open',
        new_callable=mock.mock_open,
        read_data='',
    )
    def test_list_empty(self, open_mock):
        results = self.storage.list_skills()
        assert(results == [])

    @pytest.mark.skip(reason="Not implemented")
    @mock.patch(
        'skill_storage.open',
        new_callable=mock.mock_open,
        read_data='giberish [ [ }',
    )
    def test_list_malformed(self, open_mock):
        results = FileStorage(TEST_FILE_NAME).list_skills()
        assert(results == [])

    # @mock.patch(
    #     'skill_storage.open',
    #     new_callable=mock.mock_open,
    #     read_data=json.dumps(TEST_FILE_CONTENTS),
    # )
    def test_overwrite(self):
        pass

    @mock.patch('skill_storage.FileStorage.list_skills')
    @mock.patch('skill_storage.FileStorage._overwrite_skills')
    def test_add(self, overwrite_mock, list_mock):
        NEW_FILE_CONTENTS = TEST_FILE_CONTENTS.copy()
        list_mock.return_value = NEW_FILE_CONTENTS

        self.storage.add_skill(TEST_SINGLE_SKILL)

        NEW_FILE_CONTENTS.append(TEST_SINGLE_SKILL)
        overwrite_mock.assert_called_with(NEW_FILE_CONTENTS)
