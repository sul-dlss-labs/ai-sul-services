FROM python:3.10-slim

RUN pip install intake[complete]


CMD ["intake-server", "/opt/intake/library-services-platform/folio.yml", "/opt/intake/marine-collections/collections.yml"]