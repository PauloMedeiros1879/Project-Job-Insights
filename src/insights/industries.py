from functools import lru_cache
from typing import List, Dict
from src.insights.jobs import read


@lru_cache
def get_unique_industries(path):
    job_read = read(path)
    return list(
        set(
            {
                industries["industry"]
                for industries in job_read
                if industries["industry"] != ""
            }
        )
    )


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
