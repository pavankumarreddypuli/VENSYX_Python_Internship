import csv

def read_csv(path):
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def read_txt(path):
    with open(path) as file:
        return [line.strip() for line in file.readlines()]




'''
One place to read all files
Easy to change later
Follows Single Responsibility Principle
'''