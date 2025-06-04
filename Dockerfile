FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
RUN pip install django mysqlclient gunicorn

CMD ["gunicorn", "musicprj.wsgi:application", "--bind", "0.0.0.0:8000"]
