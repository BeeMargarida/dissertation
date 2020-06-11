import csv
import sys

with open(sys.argv[1]) as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)
    ids = list()
    for row in rows:
        if len(row) > 0 and row[1] not in ids:
            ids.append(row[1])
    print(ids)
    # rows = [header] + [[row[0], row[1]] for row in rows]

# for row in rows:
#     print(row)

with open(sys.argv[2], 'w', newline='') as csvfile:
    fieldnames = ['Time'] + ids
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in rows:
        if(len(row) > 0):
            writer.writerow({'Time': row[0], row[1]: row[2]})