# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.12@sha256:1aa745fdccf56db1a56dd6a098fc5be154f1d9d05c2519fb7d2c4b3d1989da46
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
