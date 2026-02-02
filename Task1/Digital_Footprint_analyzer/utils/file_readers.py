import csv

# Reads a CSV file and returns data as a list of dictionaries
def read_csv(path):
    with open(path, newline="") as file:
        # DictReader converts each row into a dictionary
        reader = csv.DictReader(file)
        return list(reader)


# Reads a text file and returns each line as an item in a list
def read_txt(path):
    with open(path) as file:
        # Strip newline characters and return clean list
        return [line.strip() for line in file.readlines()]
