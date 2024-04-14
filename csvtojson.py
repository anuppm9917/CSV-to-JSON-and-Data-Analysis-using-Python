import csv
import json

csv_file = open("D:/Power BI/archive/calorie_info.csv", 'r')
csv_reader = csv.DictReader(csv_file)

field_names = next(csv_reader)

print(field_names)

data = []

for row in csv_reader:
    data.append(dict(zip(field_names,row.values())))

print("\nData:")
for item in data:
    print(json.dumps(item, indent=4))  # Use indentation for better readability

json_data = json.dumps(data, indent=4)

json_file = open("D:/Power BI/archive/data.json", 'w')
json_file.write(json_data)

csv_file.close()
json_file.close()