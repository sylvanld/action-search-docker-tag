FROM python:3.10-alpine

WORKDIR /app

COPY requirements.lock.txt /tmp/requirements
RUN pip install --no-cache-dir -r /tmp/requirements

COPY docker_search.py /app/docker_search.py
ENTRYPOINT [ "python", "-m", "docker_search" ]
