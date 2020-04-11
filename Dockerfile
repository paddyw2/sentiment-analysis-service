FROM tensorflow/tensorflow:2.0.1-py3

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r ./requirements.txt

COPY files ./
COPY src ./
CMD ["gunicorn", "--workers", "1", "--bind", "0.0.0.0:8080", "app:app"]
