import re
import csv
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python3 parse_doxygen_warnings.py <input_logfile> <output_csv>")
    sys.exit(1)

logfile = sys.argv[1]
outfile = sys.argv[2]

if not os.path.exists(logfile):
    print(f"Error: Input file '{logfile}' does not exist.")
    sys.exit(1)


pattern = re.compile(r'^(.*):(\d+): warning: (.*)$')
rows = []

with open(logfile, "r") as f:
    for line in f:
        match = pattern.match(line.strip())
        if match:
            file_path = match.group(1)
            line_num = match.group(2)
            message = match.group(3)
            rows.append([file_path, line_num, message])

with open(outfile, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["file", "line", "message"])
    writer.writerows(rows)

print(f"Scan {len(rows)} lines. Output saved to {outfile}")
