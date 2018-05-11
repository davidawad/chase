FROM python:3.6

EXPOSE 8000

WORKDIR /chase

COPY ./* /chase/

RUN mkdir -p /chase/state_data

COPY ./state_data/* /chase/state_data/

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "server:application", "-b", ":8000", "--log-file=-"]


# ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "/gunicorn.conf", "--log-config", "/logging.conf", "-b", ":8000", "myapp:app"]


