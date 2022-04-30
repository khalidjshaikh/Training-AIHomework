FROM alpine:latest
RUN apk update
RUN apk add bash python3 py3-pip
RUN pip install flask flask_restplus
COPY api.py /
ENTRYPOINT ["/api.py"]