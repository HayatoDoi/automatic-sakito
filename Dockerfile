FROM python:3.6
MAINTAINER HayatoDoi
RUN pip install requests beautifulsoup4 slackweb
COPY *.py /scripts/