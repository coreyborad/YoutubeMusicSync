FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install ffmpeg
RUN apt-get update
RUN apt-get install -y ffmpeg

# Install cron
RUN apt-get install -y cron