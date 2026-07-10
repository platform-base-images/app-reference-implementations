# syntax=docker/dockerfile:1
# Build stage — shell and npm available
FROM ghcr.io/platform-base-images/nodejs-base:1.0.4@sha256:b723e7e7d5f2fcf46383a991daaecb415e0e0d95484031c08af0f0b7029f8555 AS builder
USER root
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
USER nonroot

# Runtime stage — no shell, minimal attack surface
FROM ghcr.io/platform-base-images/nodejs-base:1.0.4-distroless@sha256:039947d9a79cadc14d0b382f426af7ea4a58ac846840a6f44994d8342be6b1b7
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY src/ ./src/
EXPOSE 3000
CMD ["src/index.js"]
