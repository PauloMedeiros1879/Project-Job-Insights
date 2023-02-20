from functools import lru_cache
from typing import List, Dict
from csv import DictReader


@lru_cache
def read(path):
    with open(path, mode="r") as csvfile:
        reader = DictReader(csvfile)
        return [rows for rows in reader]


def get_unique_job_types(path):
    job_read = read(path)
    return list(set({type["job_type"] for type in job_read}))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
