import csv

with open('graf.csv', 'w') as csvfile:
    fieldnames = ['hastighet', 'tid']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'hastighet': '6', 'tid': '1'})
    writer.writerow({'hastighet': '12', 'tid': '2'})
    writer.writerow({'hastighet': '24', 'tid': '3'})
