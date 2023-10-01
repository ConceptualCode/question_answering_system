FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --default-timeout=1000 -r requirements.txt --exists-action=i

EXPOSE 5000

CMD ["python", "app.py"]