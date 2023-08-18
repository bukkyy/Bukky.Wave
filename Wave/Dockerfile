# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the local code into the container at /app
COPY . /app

# Install poetry
RUN pip install poetry

# Install project dependencies using poetry
RUN poetry install

# Expose port (if your application requires a port to be exposed)
# EXPOSE <port_number>

# Command to run your application
CMD [ "sh", "-c", "poetry run python  wave1_0.py --city $CITY" ]


#To build docker image = docker build -t wave2_0 .
#To run docker docker run -it -e AWS_ACCESS_KEY_ID=youraccesskey -e AWS_SECRET_ACCESS_KEY=your secretkey -e CITY=Toronto wave2_0






