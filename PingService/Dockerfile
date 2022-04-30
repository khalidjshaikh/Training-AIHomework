FROM alpine:latest
RUN apk update
RUN apk add bash python3 py3-pip
RUN pip install flask flask_restplus
# RUN pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U 
# RUN pip install --upgrade werkzeug==0.16.1
RUN pip install --upgrade werkzeug==2.0.3
COPY api.py /
ENTRYPOINT ["/api.py"]