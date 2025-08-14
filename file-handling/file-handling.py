import os

directory = 'res'

csv_filename = os.path.join(directory, 'datafile.csv')
print(csv_filename)

rows = []

with open(csv_filename) as f:
    for line in f:
        rows.append(line.strip().split(','))


for r in rows[1:]:
    for i in range(2, len(r)):
        r[i] = float(r[i])

out_rows = []
for r in rows:
    r =[str(c) for c in r]
    out_rows.append(r)


csv_filename_out = os.path.join(directory, 'data-file-out.csv')

with open(csv_filename_out, 'w') as f:
    for r in out_rows:
        out_line = ','.join(r)
        f.write(out_line + '\n')