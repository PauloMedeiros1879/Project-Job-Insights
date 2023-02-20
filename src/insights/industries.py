from functools import lru_cache
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


def filter_by_industry(jobs, industry):
    return [filter for filter in jobs if industry == filter["industry"]]
