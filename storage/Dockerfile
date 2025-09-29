# Python base image
FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .

#install python dependecies

RUN pip install -r requirements.txt

COPY . .

# Expose the port Flask runs on

EXPOSE 9090

# ENV variables

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV DATA_DIR=/data

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=9090"]