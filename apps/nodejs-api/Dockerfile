# syntax=docker/dockerfile:1
# Build stage — shell and npm available
FROM ghcr.io/platform-images/nodejs-base:1.0.1@sha256:1815a58b41a83f57e6973f4c3c237bc7b2aca68a381362a1c6ad0a7538b17a09 AS builder
USER root
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev

# Runtime stage — no shell, minimal attack surface
FROM ghcr.io/platform-images/nodejs-base:1.0.1-distroless@sha256:da4c30aed6130f75efc51ba8792dba1a4fe022c531168495e93af76c7cb6e717
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY src/ ./src/
EXPOSE 3000
CMD ["src/index.js"]
