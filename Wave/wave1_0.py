
#import libraries - click used to create cli, pandas for data manipulation,
#os to interact with the os, boto3 to interact with AWS services, 
#botocore is raised when aws credentials are not available
#datetime to import datetime, openpyxl imports workbook, 
import click
import pandas as pd
import os
import boto3 
from botocore.exceptions import NoCredentialsError
from datetime import datetime, date
from openpyxl import Workbook
@click.command()
@click.option('--city', required=True, help='The city for weather data.')
@click.option('--startyear', default=2018, required=True, help='the beginning of the year')
@click.option('--endyear', default=2024, required=True, help='the end of the year')

#to define the main functions that fethes weather data and performs processing
def getHourlyData(city, startyear, endyear):
    if 'toronto' == city.lower():
        data=[]
        city = 31688
        for year in range(startyear, endyear):
      
          #Defines the base URL for fetching weather data from the provided endpoint.
          base_url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?"
          query_url = "format=csv&stationID={}&Year={}&timeframe=2".format(city, year)
          api_endpoint = base_url + query_url

          #Reads the CSV data from the API endpoint using pandas.
          weather_data = pd.read_csv(api_endpoint, skiprows=0)
          data.append(weather_data)
        #Concatenates the list of weather dataframes into a single dataframe.
        all_data=pd.concat(data)
        
       
        #Converts the 'Date/Time' column to a datetime format.
        all_data['Date/Time'] = pd.to_datetime(all_data['Date/Time'], errors='coerce')
        current_date = datetime.today().date()
        
        #Filters the data to keep only rows up to the current date.
        filtered_all_data = all_data[all_data['Date/Time'].dt.date <= current_date]
        filtered_all_data = filtered_all_data.dropna(subset=['Max Temp (°C)', 'Min Temp (°C)', 'Mean Temp (°C)'])
        columns_to_keep = ['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)', 'Mean Temp (°C)']

        #Drops rows with missing values in specific columns & Defines a list of columns to keep in the filtered data.
        filtered_all_data = filtered_all_data[columns_to_keep]
        
        #Writes the filtered data to a CSV file named "filtered_weather_data.csv".
        filtered_all_data.to_csv(f'filtered_weather_data.csv', index=False, header=True)      
        

        #Uploads the local CSV file to the specified S3 bucket using the upload_file method.
        s3_bucket_name = 'wave1bucket'  
        s3_file_path = 'filtered_weather_data.csv'  # Path in S3 bucket
        local_file = 'filtered_weather_data.csv' #define variable for csv file
        upload_to_s3(local_file, s3_bucket_name, s3_file_path )
def upload_to_s3(local_file, bucket, s3_file):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
    except NoCredentialsError:
        print("Credentials not available")

        
   # return filtered_all_data


#The code under this condition is executed when the script is run directly, not imported as a module.
if __name__ == '__main__':
   
   
    #Calls the getHourlyData() function to fetch and process weather data.
    dataframe = getHourlyData()
    print(dataframe.head(10)) #Prints the first 10 rows of the processed data.
    
#Th comment below indicates how to run the script from the command line, passing the --city option with the value "Toronto".
#python wave1_0.py --city Toronto 




