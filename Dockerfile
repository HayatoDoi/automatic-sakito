FROM python:3.6
MAINTAINER HayatoDoi
RUN pip install requests
RUN pip install beautifulsoup4
COPY automatic-sakito.py /scripts/automatic-sakito.py
COPY user.py /scripts/user.py
