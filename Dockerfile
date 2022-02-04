FROM python:3-alpine

WORKDIR /Engine

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","Engine.py"]
