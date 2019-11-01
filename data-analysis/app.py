import csv

print('2015: \n')
with open('C:\\Users\\asus\\Desktop\\studia syf\\5. semestr\\PSI\\Projekt\\2015.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            if line_count==0:
                print(f'Column names are: {", ".join(row)}')
                line_count+=1
            else:
                print(f'\t{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}\t{row[9]}\t{row[10]}\t{row[11]}')
                line_count += 1
            print(f'Processed {line_count} lines.')
print('2016: \n')
with open('C:\\Users\\asus\\Desktop\\studia syf\\5. semestr\\PSI\\Projekt\\2016.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            if line_count==0:
                print(f'Column names are: {", ".join(row)}')
                line_count+=1
            else:
                print(f'\t{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}\t{row[9]}\t{row[10]}\t{row[11]}')
                line_count += 1
            print(f'Processed {line_count} lines.')
print('2017: \n')
with open('C:\\Users\\asus\\Desktop\\studia syf\\5. semestr\\PSI\\Projekt\\2017.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            if line_count==0:
                print(f'Column names are: {", ".join(row)}')
                line_count+=1
            else:
                print(f'\t{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}\t{row[9]}\t{row[10]}\t{row[11]}')
                line_count += 1
            print(f'Processed {line_count} lines.')