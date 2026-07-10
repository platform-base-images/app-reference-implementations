# syntax=docker/dockerfile:1
FROM ghcr.io/platform-base-images/nginx-base:1.0.8@sha256:f5bf5c57a32b0fea7f4c027e2c8ae94ec0690212a64099595210e4ce94c5a9a5
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
