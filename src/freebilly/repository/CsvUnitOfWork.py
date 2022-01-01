import csv
from pathlib import Path
from src.freebilly.repository.CsvRepository import CsvRepository
from src.freebilly.repository.AbstractUnitOfWork import AbstractUnitOfWork
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog


class CsvUnitOfWork(AbstractUnitOfWork):

    work_logs: CsvRepository

    def __init__(self, path: Path):
        self.work_logs = CsvRepository(path=path)

    def commit(self, work_log: AbstractWorkLog) -> None:

        if work_log.is_empty():
            raise ValueError("cannot push an empty work log to repository")
        with open(
            self.work_logs.get_csv_file_path(
                work_log.get_client(), work_log.get_project()
            ),
            "w",
            newline="",
        ) as csv_file:
            work_log_writer = csv.DictWriter(
                csv_file, fieldnames=self.work_logs.get_field_names(),
            )
            work_log_writer.writeheader()
            for work_session in work_log.generate_work_sessions():
                work_log_writer.writerow(
                    {
                        "start_time": work_session.get_start_time().to_iso8601_string(),
                        "end_time": work_session.get_end_time().to_iso8601_string(),
                    }
                )

    def rollback(self):

        pass
