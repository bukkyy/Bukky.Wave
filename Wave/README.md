#Wave assessment

This file onsists of my assessment summary and reccomendations/assumptions made

## Caveats

-   In question 1, it was mentioned that the code should be executable using the command line with the year and city being the input variables. It's important to note that the current input variable is python wave1_0.py --city Toronto . The reason the YYYY variable doesn't exist is because I created the start and the end year in my command prompt at the beginning of my script. This allowed me to have all the years in one file as opposed to having different files. Also, because I am working with a specific year range


-   In Question 2, it was mentioned to provide data in the last 3  years starting from the input year 2018, however, 3 years ago from today isn't 2018. So I provided data from 2018 to 2023.


-   In Question 3, it was mentioned to join Station Inventory and Weather tables. However, when I made attempt to join these two tables, it turns out the station data doesn't have enough information to join on. The only column that I could join on is the station id and for the distinct climate ID for Toronto, only one row exists. If i had joined the table, my joined result will have two of every row. Here is my code.

-   In Question 6.1 question, it states to output Max and Min temperature for year. but wasn't specific for which year. So I wrote my code to output for each year (between 2018 and 2023)

### file def (there are 3 python files, 1 docker file, and 1.toml)

1.  wave1_0.py = This script fetches weather data, processes it, filters and saves it to a CSV file, and then uploads that CSV file to an S3 bucket. It also includes command-line options for specifying the city, start year, and end year when running the script.

2.  excel_report.py = This script downloads a CSV file from an S3 bucket, processes it using Pandas, and creates an Excel file where each year's data is stored in a separate sheet. The script can be executed using the command python excel_report.py.

3.  query.py = This file contains codes demonstrates how to download, manipulate, and analyze weather data using pandas and AWS S3 services. It performs various queries to extract insights from the data and displays the results.

4.  Dockerfile = This Dockerfile sets up the container environment, installs the required dependencies using Poetry, and runs the Python script when the container is started. It provides a reproducible and isolated environment for running the application.

5.  pyproject.toml = This pyproject.toml file serves as a central place to manage the project's metadata, dependencies, and build settings. Poetry uses this file to manage the development environment, resolve dependencies, and package your project for distribution.
