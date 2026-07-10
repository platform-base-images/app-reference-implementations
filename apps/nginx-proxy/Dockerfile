# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.5@sha256:17c060b801d103b6e40aea23e9974f39c17cde01f4cb2d945df62079e1676d89
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
