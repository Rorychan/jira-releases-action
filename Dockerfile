FROM python:latest
COPY . /app
WORKDIR /app
RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt
ENTRYPOINT ['./entrypoint.sh']