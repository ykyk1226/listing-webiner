
FROM python:3.9.1-buster

COPY settings/requirements.txt /tmp/requirements.txt
COPY settings/odbcinst.ini /etc/odbcinst.ini

RUN apt update && \
    apt -y install gcc=4:8.3.0-1 \
                   unixodbc \
                   unixodbc-dev \
                   freetds-dev \
                   freetds-bin \
                   tdsodbc && \
    export ODBCINI=/etc/odbc.ini && \
    export ODBCSYSINI=/etc && \
    export FREETDSCONF=/etc/freetds/freetds.conf && \
    pip install -r /tmp/requirements.txt && \
    mkdir -p /usr/src/listing_webiner

COPY ./listing_webiner /usr/src/listing_webiner

RUN useradd appuser && \
    chown -R appuser:appuser /usr/src/listing_webiner

WORKDIR /usr/src/listing_webiner
USER appuser

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:30000"]