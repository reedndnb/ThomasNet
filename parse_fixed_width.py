import csv
import struct
import sys

fields = []
fieldwidths = []

with open("field-layout.csv") as field_layout_in:
    reader = csv.DictReader(field_layout_in)
    for row in reader:
        fieldname = row['fieldname']
        fields.append(fieldname)
        start = int(row['start'])
        end = int(row['end'])
        calc_length = end - start + 1
        if (int(row['length']) != calc_length):
            print "Warning %s, Calculated length: %d, Given length: %s" + (fieldname, calc_length, row['length'])
        fieldwidths.append(calc_length)

print fields
print fieldwidths

def parse_line(fields, fieldwidths, line):
    field_index = 0
    d = {}
    for i, fw in enumerate(fieldwidths):
        d[fields[i]] = line[field_index:field_index + fw].strip()
        field_index = field_index + fw
    return d

with open("THOMAS.OCT15.CSV", "r") as fw_in:
    with open("THOMAS.OCT15.parsed.CSV", "w") as csv_out:
        writer = csv.DictWriter(csv_out, fields)
        writer.writeheader()
        for line in iter(fw_in):
            row = parse_line(fields, fieldwidths, line)
            writer.writerow(row)


