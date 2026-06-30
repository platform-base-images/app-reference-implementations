# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.4@sha256:6309aaee2b1f8ba042dd98f002616b2117201e23ec32a8cb59b001473edfd505
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
