FROM python:3
COPY main.py /app/
COPY requirements.txt /app/requirements.txt
ADD pip.conf /root/.pip/
RUN pip install -r /app/requirements.txt

COPY chatter.tar.gz /app/
RUN pip install /app/chatter.tar.gz
CMD ["python", "/app/main.py"]