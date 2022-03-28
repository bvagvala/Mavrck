
# importing libraries dependent to run our application
# change input and output path, run flask and input number of columns to use and column numbers like "1,2,3"
import csv
import gzip
import os
import shutil

# function to input zip and extract csv file
def extract_gz(input_path,output_path):
    # Use a breakpoint in the code line below to debug your script.
    with gzip.open(input_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
# fucntion to input columns list and read csv based on needed columns
def csv_reader(output_path,column_list):
    dict = {}
    file = open(os.path.join(output_path), "rU", encoding="utf8")
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        k = tuple([row[x] for x in column_list])
        if k in dict:
            dict[k] +=1
        else:
            dict[k] = 1
    # returning a dictionary of results
    return dict

# function to read user inputs
def user_input():
    # this accepts the user's input
    recurring_input = int(input("Welcome, input number of columns you want to read, there are upto 16 columns: "))
    column_list = []
    print("coloumns with numbers, enter which column to use one after another\n")
    print(
        "1.Company Name	 2.Crunchbase_URL	 3.url	 4.Outlet_Type	 5.Category_Groups	 6.Categories	 7.Headquarters_Location\n")
    print(
        "7.Description	 8.Crunchbase_Rank	 9.Twitter	 10.Facebook	 11.LinkedIn\n"
        "                                                                           "
        "12.Contact Email	 13.Phone Number	 14.Number of Employees	 15.Stock Symbol	 16.Stock Exchange")
    for i in range(0,recurring_input):
        column_list.append(int(input("Enter column no: "+str(i)+" to use for input:"))-1)
    return column_list
# function to print out results from group by operation
def result_out(values_dict):
    result_list = []
    for key, value in values_dict.items():
        temp_key = list(key)
        result_list.append(temp_key.append(value))
        print(temp_key)

# run the main method to run the group by application
if __name__ == '__main__':
    # input-output path for dataset, here we have a zip file, change accordingly to your local branch
    input_path = "C:\\Users\\bvagv\\Desktop\\Mavrck\\CrunchBase.gz"
    output_path = "C:\\Users\\bvagv\\Desktop\\Mavrck\\CrunchBase.csv"
    extract_gz(input_path, output_path)
    column_list = user_input()
    values_dict = csv_reader(output_path,column_list)
    result_out(values_dict)

