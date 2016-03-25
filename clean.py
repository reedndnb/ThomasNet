import csv
import sys

csv.field_size_limit(sys.maxsize)

i=0
with open("THOMAS.OCT15.CSV", "r") as in_file:
    reader = csv.reader(in_file, delimiter=' ', skipinitialspace=True)
    with open("thomasnet-cleaned.csv", "w") as out_file:
        writer = csv.writer(out_file)
        for row in reader:
            print "Line: %d" % i
            print row
            writer.writerow(row)
            i += 1



