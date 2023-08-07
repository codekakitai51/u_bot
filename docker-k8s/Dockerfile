# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./generate_tweets.py /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir boto3 tweepy markovify

# Run app.py when the container launches
CMD ["python", "/app/generate_tweets.py"]