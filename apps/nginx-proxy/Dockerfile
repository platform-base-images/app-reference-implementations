# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.0@sha256:71e16be919ca3d67deb7d2cd460eedfda87d3edb86280c3b01ed94e73c98328b
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
