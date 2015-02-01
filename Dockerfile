FROM python:3.4.2-onbuild

ENV INFLUXDB_PROTO http
ENV INFLUXDB_HOST influxdb
ENV INFLUXDB_PORT 8086
ENV INFLUXDB_DB_NAME test_db
ENV INFLUXDB_USER root
ENV INFLUXDB_PASS root
ENV STATUS_INTERVAL 10

CMD [ "python", "./sine.py" ]
