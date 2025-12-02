FROM python:3.11-slim AS builder
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates gcc g++ libc6-dev make && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . /app

RUN python -m pytest -q

FROM python:3.11-slim AS runtime
WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    pip install --no-cache-dir -r requirements.txt

COPY --from=builder /app/src /app/src
COPY --from=builder /app/Datapoints.json /app/src/Datapoints.json

RUN useradd -m -u 1000 iec104user && chown -R iec104user:iec104user /app
USER iec104user

EXPOSE 2404

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import socket; s=socket.socket(); s.settimeout(5); s.connect(('localhost', 2404)); s.close()" || exit 1

CMD ["python", "src/batch_server.py"]