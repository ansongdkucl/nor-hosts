
import csv
with open('danhosts1.csv', 'r',encoding='latin-1') as f:
     readCSV = csv.reader(f, delimiter=',')
     for row in readCSV:
        #grab variables from csv

        ip = row[0]
        hostname = row[1]
        router = row[2]
        vendor = row[3]
        building = row[4]
        cab = row[5]


        print(ip + ':')
        #print(ip,'{}'.format(':'))
        print("  hostname: {}".format(hostname))
        print("  port: 22")
        print("  platform: {}".format(vendor))
        print("  groups:")
        print('      - {}'.format(router))
        print('  data:')
        print('    building: {}'.format(building))
        print('    CAB: {}'.format(cab))

        print('\n')
