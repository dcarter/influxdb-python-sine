FROM python:3.4.2-onbuild

ENV INFLUXDB_PORT_8086_TCP_PROTO http
#ENV INFLUXDB_PORT_8086_TCP_ADDR localhost
#ENV INFLUXDB_PORT_8086_TCP_PORT 8086
#ENV INFLUXDB_ENV_PRE_CREATE_DB test_db
ENV INFLUXDB_USER root
ENV INFLUXDB_PASS root
ENV STATUS_INTERVAL 10

CMD [ "python", "./sine.py" ]
