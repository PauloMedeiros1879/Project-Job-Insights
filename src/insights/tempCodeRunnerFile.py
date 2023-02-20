def read(path):
    with open(path, mode="r") as csvfile:
        reader = DictReader(csvfile)
        return [rows for rows in reader]