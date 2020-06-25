import csv
import sys

with open(sys.argv[1]) as f, open(sys.argv[2], 'w', newline='') as csvfile:
    reader = csv.reader(f)
    header = next(reader)
    del header[0]

    data = list(reader)

    fieldnames = ['Time'] + header
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    last_entry = dict()

    t0 = 1592334347000
    delta = 0

    for i in range(0,250):
        print("IT", i)
        t1 = t0 + delta
        row = {'Time': int(((t1-1592334347000)/1000))}
        for idx, val in enumerate(header):
            row[val] = 0
            for r in data:
                if (val not in last_entry or last_entry[val] <= int(r[0])) and int(r[0]) <= t1 and r[idx + 1]:
                    last_entry[val] = int(r[0])
                    row[val] = r[idx + 1]
        last_entry = dict()
        writer.writerow(row)
        delta = delta + 5000