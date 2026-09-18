# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.17@sha256:9af54ed533cc677139c5bf39ce71591274d5e55b79b350474351d3d3a6b72c75
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
