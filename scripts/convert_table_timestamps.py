import csv
import sys

with open(sys.argv[1]) as f, open(sys.argv[2], 'w', newline='') as csvfile:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)
    ids = list()

    for row in rows:
        if len(row) > 0 and row[0] not in ids:
            ids.append(row[0])

    nrs = dict()

    fieldnames = ['Time'] + ids
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in rows:
        if(len(row) > 0):
            if row[0] not in nrs:
                nrs[row[0]] = 0

            nrs[row[0]] = nrs[row[0]] + 1
            writer.writerow({'Time': row[1], row[0]: nrs[row[0]]})
