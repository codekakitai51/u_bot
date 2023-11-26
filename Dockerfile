# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install MeCab and its dependencies
RUN apt-get update && apt-get install -y mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file sudo

# Install neologd
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y -p /usr/local/lib/mecab/dic/mecab-ipadic-neologd \
    && echo "mecab-ipadic-neologd installation complete"

# Update the MeCab dictionary to mecab-ipadic-neologd
ENV MECABRC /etc/mecabrc
RUN sed -i '/dicdir =/d' $MECABRC && echo "dicdir = /usr/local/lib/mecab/dic/mecab-ipadic-neologd" >> $MECABRC

# Install any needed packages
RUN pip install boto3 markovify tweepy requests mecab-python3
