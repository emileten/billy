import os
from tempfile import TemporaryDirectory, NamedTemporaryFile
from pathlib import Path
import pytest
from src.freebilly.repository.CsvRepository import CsvRepository
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog
from src.freebilly.domain.SetWorkLog import SetWorkLog


# TODO duplicate stuff, consider fixtures

def test_exists():
    temp_folder_path = '/tmp'
    with NamedTemporaryFile(dir=temp_folder_path) as temp_fp:
        os.rename(temp_fp.name,
                  str(Path().joinpath(temp_folder_path, 'work_log_A_1.csv')))  # because no full name choice option
        repo = CsvRepository(Path('/tmp'))
        assert repo.exists('A', '1')
        os.rename(str(Path().joinpath(temp_folder_path, 'work_log_A_1.csv')), temp_fp.name)  # finally, rename back


def test_exists_push():
    with TemporaryDirectory() as fake_dir_path:
        repo = CsvRepository(Path(fake_dir_path))
        empty_work_log = SetWorkLog(client='A', project='1')
        repo.push(empty_work_log)
        assert repo.exists('A', '1')


def test_exists_get():
    temp_folder_path = '/tmp'
    with NamedTemporaryFile(dir=temp_folder_path) as temp_fp:
        os.rename(temp_fp.name,
                  str(Path().joinpath(temp_folder_path, 'work_log_A_1.csv')))  # because no full name choice option
        repo = CsvRepository(Path('/tmp'))
        assert repo.exists('A', '1')
        my_work_log: repo.get('A', '1')
        assert isinstance(my_work_log, AbstractWorkLog)
        assert my_work_log.is_empty()
        os.rename(str(Path().joinpath(temp_folder_path, 'work_log_A_1.csv')), temp_fp.name)  # finally, rename back


def test_get_fails():
    repo = CsvRepository(Path('/tmp'))
    with pytest.raises(ValueError):
        repo.get('A', '1')
