import csv
import sys

with open(sys.argv[1]) as f, open(sys.argv[2], 'w', newline='') as csvfile:
    reader = csv.reader(f)
    header = next(reader)
    del header[0]

    data = list(reader)

    fieldnames = ['Time', 'Active', 'Inactive']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    last_entry = dict()

    t0 = 1593036879000
    delta = 0

    for it in range(0,450):
        print("IT", it)
        t1 = t0 + delta
        row = {'Time': int(((t1-1593036879000)/1000))}
        active = dict()
        inactive = dict()
        for idx, val in enumerate(header):
            for r in data:
                if (val not in last_entry or last_entry[val] <= int(r[0])) and int(r[0]) <= t1 and r[idx + 1]:
                    last_entry[val] = int(r[0])

                    for i in range(1, len(r) - 1):
                        if not r[i]: continue
                        elif int(r[i]) == 1:
                            active[val] = 1
                            inactive.pop(val, None)
                        elif int(r[i]) == 0:
                            inactive[val] = 1
                            active.pop(val, None)
        last_entry = dict()
        row['Active'] = len(active.keys())
        row['Inactive'] = len(inactive.keys())
        writer.writerow(row)
        delta = delta + 5000