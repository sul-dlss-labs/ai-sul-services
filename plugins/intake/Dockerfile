FROM python:3.10-slim

RUN pip install intake[complete]

COPY plugins/intake/conf.yaml .

CMD ["intake-server", "conf.yaml"]