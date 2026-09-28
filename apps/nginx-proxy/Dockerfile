# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.18@sha256:4b36dfcd1c2dd8d86cc284e1faf258fb48dba0c664ead82f7201842bcd840b39
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
