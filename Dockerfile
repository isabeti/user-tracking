FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirments.txt requirments.txt
RUN pip3 install -r requirments.txt
