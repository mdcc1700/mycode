import pandas

def main():

    # create a dataframe from json
    df = pandas.read_json("5movies.json")

    # create a dataframe from csv
    df = pandas.read_csv("5movies.csv")


    # writeout dataframe to CSV
    df.to_csv("5movies-translated-from-json.csv")

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")


