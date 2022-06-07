FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /comics
COPY requirements.txt /comics/requirements.txt
RUN pip install -r requirements.txt
COPY . /comics
