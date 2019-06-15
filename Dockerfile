FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install ffmpeg
RUN apt-get update
RUN apt-get install -y ffmpeg

# Install cron
RUN apt-get install -y cron

# Add crontab file in the cron directory
COPY crontabfile /etc/cron.d/task-cron
RUN chmod 0644 /etc/cron.d/task-cron
RUN touch /var/log/cron.log
RUN crontab /etc/cron.d/task-cron

# Adjust timezone
RUN echo "Asia/Taipei" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

CMD /etc/init.d/cron start && tail -f /var/log/cron.log