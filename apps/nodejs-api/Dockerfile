# syntax=docker/dockerfile:1
# Build stage — shell and npm available
FROM ghcr.io/platform-base-images/nodejs-base:1.0.9@sha256:df7adfc0928a6970a95a8f32f2ed22fe3650793deb243a4c091c62faf86de26e AS builder
USER root
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
USER nonroot

# Runtime stage — no shell, minimal attack surface
FROM ghcr.io/platform-base-images/nodejs-base:1.0.9-distroless@sha256:fe2c1723da8c9623e5b87100bb9990ef24b9dc9b4a8f5caf336887a26edb94a9
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
