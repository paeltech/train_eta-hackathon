#Importing CSV module
import csv


#reading distance data from given CSV file
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    #Check sensor readins
    data_check(reader)

def data_check(reader):
    dt = 0
    dr = 0
    for line in reader:
        dt += float(line["distance_travelled"])
        # dr -= float(line["distance_remaining"])
    print dt - 1011.7959
    # print dr



if __name__ == "__main__":
    with open("at_distance_sensors.csv") as f_obj:
        csv_dict_reader(f_obj)
