import os
import csv
from tempfile import TemporaryDirectory, NamedTemporaryFile
from pathlib import Path
import pytest
import pendulum as pdl
import ordered_set
from src.freebilly.repository.CsvRepository import CsvRepository
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog
from src.freebilly.domain.OrderedSetWorkLog import OrderedSetWorkLog
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession

# TODO there is a LOT, LOT of duplicate stuff, consider fixtures, but it's hard because of context managers. Oh. Consider having a util func with a context manager that YIELDS.

def test_manually_written_csv_exists(): # other tests depend on this success
    temp_folder_path = '/tmp'
    with NamedTemporaryFile(dir=temp_folder_path) as temp_fp:
        csv_path = str(Path().joinpath(temp_folder_path, 'work_log_A_1.csv'))
        os.rename(temp_fp.name,
                  csv_path)  # because no full name choice option
        with open(csv_path, 'w', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['start_time', 'end_time'])
            csvwriter.writerow([pdl.now().to_iso8601_string(), pdl.now().to_iso8601_string()]) #TODO coupling with pendulum
        repo = CsvRepository(Path('/tmp'))
        assert repo.exists('A', '1')
        assert not repo.exists('B', '1')
        os.rename(csv_path, temp_fp.name)  # finally, rename back

def test_valid_csv_is_valid(): #TODO this is almost entirely a duplicate of test_exists()
    temp_folder_path = '/tmp'
    with NamedTemporaryFile(dir=temp_folder_path) as temp_fp:
        csv_path = str(Path().joinpath(temp_folder_path, 'work_log_A_1.csv'))
        os.rename(temp_fp.name,
                  csv_path)  # because no full name choice option
        with open(csv_path, 'w', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['start_time', 'end_time'])
            csvwriter.writerow([pdl.now().to_iso8601_string(), pdl.now().to_iso8601_string()]) #TODO coupling with pendulum
        repo = CsvRepository(Path('/tmp'))
        assert repo.valid('A', '1')
        os.rename(csv_path, temp_fp.name)  # finally, rename back


def test_bad_column_csv_is_not_valid(): #TODO this is almost entirely a duplicate of test_valid()
    temp_folder_path = '/tmp'
    with NamedTemporaryFile(dir=temp_folder_path) as temp_fp:
        csv_path = str(Path().joinpath(temp_folder_path, 'work_log_A_1.csv'))
        os.rename(temp_fp.name,
                  csv_path)  # because no full name choice option
        with open(csv_path, 'w', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['bad_name', 'end_time'])
            csvwriter.writerow([pdl.now().to_iso8601_string(), pdl.now().to_iso8601_string()]) #TODO coupling with pendulum
        repo = CsvRepository(Path('/tmp'))
        assert not repo.valid('A', '1')
        os.rename(csv_path, temp_fp.name)  # finally, rename back

def test_empty_csv_is_not_valid(): #TODO this is almost entirely a duplicate of test_valid()
    temp_folder_path = '/tmp'
    with NamedTemporaryFile(dir=temp_folder_path) as temp_fp:
        csv_path = str(Path().joinpath(temp_folder_path, 'work_log_A_1.csv'))
        os.rename(temp_fp.name,
                  csv_path)  # because no full name choice option
        with open(csv_path, 'w', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['start_time', 'end_time'])
        repo = CsvRepository(Path('/tmp'))
        assert not repo.valid('A', '1')
        os.rename(csv_path, temp_fp.name)  # finally, rename back

# def test_newly_pushed_log_exists():
#     with TemporaryDirectory() as fake_dir_path:
#         repo = CsvRepository(Path(fake_dir_path))
#         my_work_session = PendulumWorkSession(start_time=pdl.datetime(1, 1, 1), end_time=pdl.datetime(1, 2, 2))
#         non_empty_work_log = OrderedSetWorkLog(client='A', project='1', sessions=ordered_set.OrderedSet([my_work_session]))
#         repo.push(non_empty_work_log)
#         assert repo.exists(client='A', project='1')

# def test_pushing_empty_log_fails():
#     with TemporaryDirectory() as fake_dir_path:
#         repo = CsvRepository(Path(fake_dir_path))
#         empty_work_log = OrderedSetWorkLog(client='A', project='1')
#         with pytest.raises(ValueError):
#             repo.push(empty_work_log)


def test_can_get_log_from_manually_written_csv():
    temp_folder_path = '/tmp'
    my_work_session = PendulumWorkSession(start_time=pdl.datetime(1, 1, 1), end_time=pdl.datetime(1, 2, 2))
    with NamedTemporaryFile(dir=temp_folder_path) as temp_fp:
        os.rename(temp_fp.name,
                  str(Path().joinpath(temp_folder_path, 'work_log_A_1.csv')))  # because no full name choice option
        with open(
            str(Path().joinpath(temp_folder_path, 'work_log_A_1.csv')), "w", newline="",
        ) as csv_file:
            my_writer = csv.DictWriter(
                csv_file,
                fieldnames=["start_time", "end_time"],
            )
            my_writer.writeheader()
            my_writer.writerow(
                {
                    "start_time": my_work_session.get_start_time().to_iso8601_string(),
                    "end_time": my_work_session.get_end_time().to_iso8601_string(),
                }
            )

        repo = CsvRepository(Path('/tmp'))
        my_work_log = repo.get('A', '1')
        assert isinstance(my_work_log, AbstractWorkLog)
        assert my_work_session in my_work_log
        os.rename(str(Path().joinpath(temp_folder_path, 'work_log_A_1.csv')), temp_fp.name)  # finally, rename back


def test_getting_non_existing_log_from_repo_fails():
    repo = CsvRepository(Path('/tmp'))
    with pytest.raises(ValueError):
        repo.get('A', '1')

# def test_can_get_log_pushed_through_repo():
#     with TemporaryDirectory() as fake_dir_path:
#         repo = CsvRepository(Path(fake_dir_path))
#         my_work_session = PendulumWorkSession(start_time=pdl.datetime(1, 1, 1), end_time=pdl.datetime(1, 2, 2))
#         non_empty_work_log = OrderedSetWorkLog(client='A', project='1', sessions=ordered_set.OrderedSet([my_work_session]))
#         repo.push(non_empty_work_log)
#         assert repo.exists('A', '1')
#         retrieved_log = repo.get('A', '1')
#         assert my_work_session in retrieved_log


# def test_can_get_csv_path_of_log_from_repo():
#     with TemporaryDirectory() as fake_dir_path:
#         repo = CsvRepository(Path(fake_dir_path))
#         my_work_session = PendulumWorkSession(start_time=pdl.datetime(1, 1, 1), end_time=pdl.datetime(1, 2, 2))
#         non_empty_work_log = OrderedSetWorkLog(client='A', project='1', sessions=ordered_set.OrderedSet([my_work_session]))
#         repo.push(non_empty_work_log)
#         assert repo.get_csv_file_path('A','1') == str(Path(fake_dir_path).joinpath('work_log_A_1.csv'))
#
#
