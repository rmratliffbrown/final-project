FROM python:3.9-slim

WORKDIR /app

# COPY . /app
RUN pip install --upgrade pip

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY ./app.py /app
COPY ./model.py /app


EXPOSE 8080

CMD ["python", "app.py"]
