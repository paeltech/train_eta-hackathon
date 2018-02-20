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
    dr = 1011.7959
    for line in reader:
        dt += float(line["distance_travelled"])
        # dr -= float(line["distance_remaining"])
    print dt - dr

    #Write to file if there is a problem
    #if dt - dr == dr:
    #    print ("there is no problem in sensor readings")

def power_check(reader):
    for line in reader:
        if line["power_supply"] > 0.995 or line["power_supply == 1"]:
            #write the error to file
            print ("There is power fluctuation at {}", format(line))



if __name__ == "__main__":
    with open("at_distance_sensors.csv") as f_obj:
        csv_dict_reader(f_obj)

if __name__ == "__main__":
    with open("at_power_sensors.csv") as f_obj1:
        csv_dict_reader(f_obj1)
