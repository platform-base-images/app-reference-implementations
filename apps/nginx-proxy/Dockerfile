# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.14@sha256:a4473d086b7438a0e733d0ffac6c6dcee3527137e44c9b6017861926bc0dc48d
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
