FROM python:latest
COPY . /app
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt
ENTRYPOINT ['./entrypoint.sh']