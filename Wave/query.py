import boto3
import pandas as pd

# To Set AWS credentials (using environment variables is recommended)
aws_access_key_id = 'AKIAR26AZN6SSXLWVBEF'
aws_secret_access_key = '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'

# Initializing the S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Specifying the S3 bucket and file path
s3_bucket_name = 'wave1bucket'  # Replace with your S3 bucket name
s3_file_path = 'filtered_weather_data.csv'  # Path in S3 bucket
local_file = 'filtered_weather_data.csv'

# Downloading the file from S3 and read it into a DataFrame
s3.download_file(s3_bucket_name, s3_file_path, local_file)
df = pd.read_csv(local_file)

# Converting 'Date/Time' to datetime format
df['Date/Time'] = pd.to_datetime(df['Date/Time'], format='%Y-%m-%d')

# Performing queries on the DataFrame
# For example, get the maximum and minimum temperature for a specific year
grouped_data = df.groupby(df['Date/Time'].dt.year).agg({'Max Temp (°C)': 'max', 'Min Temp (°C)': 'min'})

print("Year\tMax Temp\tMin Temp")
print(grouped_data)


#Queryquestion 1
# Calculate the average daily temperature for each year
average_temp_per_year = df.groupby(df['Date/Time'].dt.year)['Mean Temp (°C)'].mean()

#Queryquestion 2
# Calculate the average of the previous two years' temperatures for each year
average_previous_two_years = average_temp_per_year.shift(1).rolling(window=2).mean()
# Calculate the percentage difference between the current year and the average of the previous two years
percentage_difference = ((average_temp_per_year - average_previous_two_years) / average_previous_two_years) * 100
# Combine the results into a DataFrame
result_df = pd.DataFrame({
    'Year': average_temp_per_year.index,
    'Average Temperature': average_temp_per_year.values,
    'Average of Previous Two Years': average_previous_two_years.values,
    'Percentage Difference (%)': percentage_difference.values
})

print(result_df)

#Queryquestion 3
# Calculate the average temperature per month for each year
df['Year'] = df['Date/Time'].dt.year
df['Month'] = df['Date/Time'].dt.month
average_temp_per_month = df.groupby(['Year', 'Month'])['Mean Temp (°C)'].mean().reset_index()
# Calculate the difference between the average temperature for each month and the previous year's average temperature for the same month
average_temp_per_month['Difference'] = average_temp_per_month.groupby('Month')['Mean Temp (°C)'].diff()

print(average_temp_per_month)

#This comment below indicates how to run the script from the command line
#python query.py
