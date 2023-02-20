from functools import lru_cache
from csv import DictReader


@lru_cache
def read(path):
    with open(path, mode="r") as csvfile:
        reader = DictReader(csvfile)
        return [rows for rows in reader]


def get_unique_job_types(path):
    job_read = read(path)
    return list(set({type["job_type"] for type in job_read}))


def filter_by_job_type(jobs, job_type):
    return [type for type in jobs if job_type == type["job_type"]]
