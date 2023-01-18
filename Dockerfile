# We will use python:3.10-alpine as the base image for building the Flask container
FROM python:3.10-alpine

# It specifies the working directory where the Docker container will run
WORKDIR /app

# Copying the requirement files to the working directory
COPY requirements.txt requirements.txt

# Install all the dependencies required to run the Flask application
RUN pip3 install -r requirements.txt

# Copying all the application files to the working directory
COPY . .

# The command required to run the Dockerized application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]