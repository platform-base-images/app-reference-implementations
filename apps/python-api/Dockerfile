# syntax=docker/dockerfile:1
# Build stage — pip available
FROM ghcr.io/platform-base-images/python-base:1.0.14@sha256:2f2a552a1b9c78d5794d2e17e122ee2f07fc14b427ce899464bfb979ee33b586 AS builder
USER root
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/app/packages -r requirements.txt
USER nonroot

# Runtime stage — python-base has no distroless variant currently (Chainguard's
# distroless python image was stuck on an unpatched python-3.14 with no shell to
# work around it; see platform-base-images/hardened-base). Using the standard
# variant here instead.
FROM ghcr.io/platform-base-images/python-base:1.0.14@sha256:2f2a552a1b9c78d5794d2e17e122ee2f07fc14b427ce899464bfb979ee33b586
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
CMD ["python3", "/app/src/main.py"]
