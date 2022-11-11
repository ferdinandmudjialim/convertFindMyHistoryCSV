#!/usr/bin/env/python3
# Ferdinand Mudjialim, 2022-11

import argparse, pathlib, csv
from datetime import datetime


parser = argparse.ArgumentParser(description='Convert FindMyHistory CSVs to importable Google My Maps CSV.')
parser.add_argument('-f', '--file', help='input file', required=True)
args = parser.parse_args()

output_cols = ['baUUID', 'batteryLevel', 'batteryStatus', 'deviceDiscoveryId', 'deviceDisplayName', 'deviceModel', 'id', 'identifier', 'altitude', 'floorLevel', 'horizontalAccuracy', 'isInaccurate', 'isOld', 'latitude', 'locationFinished', 'longitude', 'positionType', 'timeStamp', 'verticalAccuracy', 'modelDisplayName', 'name', 'prsId', 'serialNumber']

def main(): 
    with open(args.file) as csv_file: 
        with open(args.file.split('.csv')[0] + '_google.csv', 'w') as out_file: 
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_writer = csv.writer(out_file)
           
            # start writing csv
            csv_writer.writerow(output_cols)
            
            # read csv
            line_count = 0 
            for row in csv_reader: 
                if line_count == 0: 
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1 
                else: 
                    # gotta convert the unix timestamps to utc (index 17) 
                    csv_writer.writerow(row[:17]+[datetime.utcfromtimestamp(int(row[17])/1000).strftime('%Y-%m-%d %H:%M:%S')]+row[18:])
                    line_count += 1 
            print(f'Processed {line_count} lines.') 
            
            


if __name__=='__main__':
    main()
