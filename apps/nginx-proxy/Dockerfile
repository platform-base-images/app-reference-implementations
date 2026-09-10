# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.16@sha256:e043af30a18c2656ec604224c51084e4b7fb718035288adcb8a270d8222a7311
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
