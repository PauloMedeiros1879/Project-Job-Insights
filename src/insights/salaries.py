from functools import lru_cache
from src.insights.jobs import read


@lru_cache
def get_max_salary(path):
    job_read = read(path)
    return max(
        [
            int(salary["max_salary"])
            for salary in job_read
            if salary["max_salary"].isdigit()
        ]
    )


def get_min_salary(path):
    job_read = read(path)
    return min(
        [
            int(salary["min_salary"])
            for salary in job_read
            if salary["min_salary"].isdigit()
        ]
    )


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("not exist")

    if (
        not float(str(job["min_salary"])).is_integer()
        or not float(str(job["max_salary"])).is_integer()
        or not str(salary).replace("-", "").isnumeric()
    ):
        raise ValueError("one of the salaries is not valid")

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("min_salary is bigger then max_salary")

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(jobs, salary):
    filter_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_salary.append(job)
        except ValueError as err:
            print(err)

    return filter_salary
