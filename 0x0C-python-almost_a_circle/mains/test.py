#!/usr/bin/python3
import csv

data = [
    {'Name': 'Alice', 'Age': 25, 'Country': 'USA'},
    {'Name': 'Bob', 'Age': 30, 'Country': 'Canada'}
]

# Serializing data to CSV format
formatted_data = []
for person in data:
    formatted_person = f'Person: ({person["Name"]}), ({person["Age"]}), ({person["Country"]})'
    formatted_data.append(formatted_person)

# Joining the formatted strings into a single string separated by newline characters
serialized_data = '\n'.join(formatted_data)


# Now, csv_string contains the serialized CSV data
print(serialized_data)
