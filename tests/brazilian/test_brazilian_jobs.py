from src.pre_built.brazilian_jobs import read_brazilian_file

path = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():

    jobsBr = read_brazilian_file(path)

    for dictionary in jobsBr:
        assert "title" in dictionary
        assert "salary" in dictionary
        assert "type" in dictionary
