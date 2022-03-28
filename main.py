
# importing libraries dependent to run our application
# change input and output path, run flask and input number of columns to use and column numbers like "1,2,3"

import csv
import gzip
import os
import shutil
from flask import Flask
from flask_restful import Resource, Api

# creating API application with flask
app = Flask(__name__)
api = Api(app)

# class for API
class Groupby(Resource):
    # get method, parsing information of number of columns, column numbers to be used in the API
    def get(self, value, column_info):
        if value:
            if column_info:
                # input-output path for dataset, here we have a zip file, change accordingly to your local branch
                input_path = "C:\\Users\\bvagv\\Desktop\\Mavrck\\CrunchBase.gz"
                output_path = "C:\\Users\\bvagv\\Desktop\\Mavrck\\CrunchBase.csv"
                extract_gz(input_path, output_path)
                column_list = user_input(value, column_info)
                values_dict = csv_reader(output_path, column_list)
                # returning a dictionary of results
                return values_dict
            else:
                # alternative results for output
                return "Not found", 404
        else:
            return "Not found", 404
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
    return dict
# function to read user inputs
def user_input(value, column_info):
    # this accepts the user's input
    recurring_input = value
    column_list = []
    for i in range(0,recurring_input):
        column_list.append(int(column_info[i])-1)
        column_info+= 1
    return column_list
# function to Generate/print/write out results from the group by

def result_out(values_dict):
    result_list = []
    for key, value in values_dict.items():
        temp_key = list(key)
        result_list.append(temp_key.append(value))
        print(temp_key)
api.add_resource(Groupby, '/Groupby/<value><column_info>')

# main function, which needs to be run to use our API
if __name__ == '__main__':
    app.run()
    input_path = "C:\\Users\\bvagv\\Desktop\\Mavrck\\CrunchBase.gz"
    output_path = "C:\\Users\\bvagv\\Desktop\\Mavrck\\CrunchBase.csv"
    # extract_gz(input_path, output_path)
    # sample user input
    column_list = user_input(0, "1,2,3,4,5")
    values_dict = csv_reader(output_path,column_list)
    result_out(values_dict)

