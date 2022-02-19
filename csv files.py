import csv


# with open("Neeraj.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)     # To read a csv file

with open("Neeraj.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)   # Read csv file as dictionary

    for line in csv_reader:                 # to print lines of the file
        print(line)

    with open("new_names.csv", "w") as new_file:
        filenames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnames=filenames, delimiter='\t')
        csv_writer.writeheader()        # Adds header

        # csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)       
