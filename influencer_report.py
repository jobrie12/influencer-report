import pandas as pd
import sys
import argparse
from operator import itemgetter
import json

parser = argparse.ArgumentParser()
parser.add_argument("input", help="The csv, xls, xlsx file that needs\
                    processing", type=str)
parser.add_argument("--output", help="Will write the aggregated list to this\
                    location/file or else will write to .json file same\
                    as input", type=str)

file = pd.ExcelFile("john-doe-ir.xls")
sheets = pd.read_excel(file, None)
records = []
for key in sheets.keys():
    if key != "All portraits":
        dictionary = sheets[key].to_dict(orient='records')
        for record in dictionary:
            if record['Followers'] is not None:
                record['ALT Benchmark follower percentage'] = \
                record['Followers'] / 330000000
                record['Blended Follower %'] = \
                (record['Benchmark follower percentage'] + \
                record['ALT Benchmark follower percentage']) / 2
                record['Blended Score'] = \
                record['Audience follower percentage'] - \
                record['Blended Follower %']
            else:
                record['ALT Benchmark follower percentage'] = 0
                record['Blended  Follower %'] = 0
                record['Blended Score'] = 0
            if record['Blended Score'] >= 0.01:
                record['Category'] = key
                records.append(record)

sorted_records = sorted(records, key=itemgetter('Blended Score'), reverse=True)

f = open("john-doe-ir.json", "w")
f.write(json.dumps(sorted_records, indent=1))
f.close()

args = parser.parse_args()
if args.output:
    print(args.output)


