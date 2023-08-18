

import boto3
import pandas as pd
# Creating an S3 access object
obj = boto3.client("s3")
# Downloading a csv file 
# from S3 bucket to local folder
obj.download_file(
    Filename="/Users/bukkyo/Wave/DownloadedFile.csv",
    Bucket="wave1bucket",
    Key="filtered_weather_data.csv"
)

# create a excel writer object

# Reads the downloaded CSV file into a Pandas DataFrame named df.
df = pd.read_csv("downloadedFile.csv")

#  Converts the 'Date/Time' column in the DataFrame to a datetime format with the specified format.
df['Date/Time'] = pd.to_datetime(df['Date/Time'], format= '%Y-%m-%d')

# Specifies the path for the output Excel file that will be created.
output_file_path = "path to filtered_weather_data_excel.xlsx"  # Specify the output file path

#Creates an Excel writer object using the specified output file path. The with statement ensures that the Excel writer is properly closed after use.
with pd.ExcelWriter(output_file_path) as writer:
    
    # Iterates through unique years present in the 'Date/Time' column of the DataFrame.
    for year in df['Date/Time'].dt.year.unique():
      
      #Filters the DataFrame to include only rows corresponding to the current year
      data_frame_year = df[df['Date/Time'].dt.year == year]
       
        # Use to_excel function to store the dataframe in specified sheet
      data_frame_year.to_excel(writer, sheet_name=str(year), index=False)

#This comment below indicates how to run the script from the command line 
#python excel_report.py
