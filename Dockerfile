FROM python:3.6
MAINTAINER HayatoDoi
RUN pip install requests beautifulsoup4 slackweb
COPY automatic-sakito.py /scripts/automatic-sakito.py
COPY user.py /scripts/user.py
