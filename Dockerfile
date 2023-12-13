# Use the Google Cloud SDK image as the base image
FROM gcr.io/google.com/cloudsdktool/cloud-sdk:latest

# Install Python and other dependencies
RUN apt-get update && apt-get install -y python3-pip python3-dev mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file sudo

# Install neologd
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y -p /usr/local/lib/mecab/dic/mecab-ipadic-neologd \
    && echo "mecab-ipadic-neologd installation complete"

# Update the MeCab dictionary to mecab-ipadic-neologd
ENV MECABRC /etc/mecabrc
RUN sed -i '/dicdir =/d' $MECABRC && echo "dicdir = /usr/local/lib/mecab/dic/mecab-ipadic-neologd" >> $MECABRC

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install required Python packages
RUN pip install boto3 markovify tweepy requests mecab-python3 google-cloud-storage
