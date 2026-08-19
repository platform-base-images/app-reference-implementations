# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.13@sha256:0021085356b128eaebae2cf0d20f26f4d5211a43f798f210de5d57b1bc8612a7
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
