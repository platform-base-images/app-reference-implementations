# syntax=docker/dockerfile:1
# Build stage — pip available
FROM ghcr.io/platform-base-images/python-base:1.0.4@sha256:fe7742c15d0476735df93515cb1085722c8982e81f9f583b8a4f4d2149a1811c AS builder
USER root
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/app/packages -r requirements.txt

# Runtime stage — no shell, no pip
FROM ghcr.io/platform-base-images/python-base:1.0.3-distroless
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
WORKDIR /app
COPY --from=builder /app/packages ./packages
COPY src/ ./src/
ENV PYTHONPATH=/app/packages
EXPOSE 8000
CMD ["/app/src/main.py"]
