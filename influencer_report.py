import pandas as pd
import sys
import argparse
from operator import itemgetter
import json
import os.path

parser = argparse.ArgumentParser()
parser.add_argument("input", help="The csv, xls, xlsx file that needs\
                    processing", type=str)
parser.add_argument("--output", help="Will write the aggregated list to this\
                    location/file or else will write to .json file same\
                    as input", type=str)
args = parser.parse_args()
if args.output:
    print(args.output)
    
file = pd.ExcelFile(args.input)
sheets = pd.read_excel(file, None)
records = []
usernameList = []
for key in sheets.keys():
    if key != "All portraits":
        dictionary = sheets[key].to_dict(orient='records')
        for record in dictionary:
            if record['Username'] in usernameList:
                print('Duplicate found -- {} in {} category left out'
                      .format(record['Name'], key))
            else :
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
                    usernameList.append(record['Username'])

sorted_records = sorted(records, key=itemgetter('Blended Score'), reverse=True)

filename = os.path.splitext(args.input)[0]
f = open("{}.json".format(filename), "w")
f.write(json.dumps(sorted_records, indent=1))
f.close()




