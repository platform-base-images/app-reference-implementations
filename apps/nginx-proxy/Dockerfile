# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.23@sha256:6312d9bc1027f12f01c8aad772737580f7990ec42fd942798913fc1d4b8bdf03
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
