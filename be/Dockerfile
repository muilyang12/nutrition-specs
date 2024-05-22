FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV IS_PROD=True
ENV PYTHONUNBUFFERED=1

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "config.wsgi:application"]
