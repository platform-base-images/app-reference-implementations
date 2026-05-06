# syntax=docker/dockerfile:1
FROM ghcr.io/platform-images/nginx-base:1.0.1@sha256:98c75244b591ef93d1b976318b7685f6f165e114181fe53f285da3def1c8802d
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
