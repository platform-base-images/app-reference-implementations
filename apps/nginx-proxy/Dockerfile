# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.15@sha256:1174af1f215bad035b13cfcf74a22720f0714bf6553e281f653403503d1e5ef4
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
