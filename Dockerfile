FROM python:3.6
RUN mkdir /myapp
WORKDIR /myapp
COPY requirements.txt /myapp/
RUN pip install -r requirements.txt
EXPOSE 5000