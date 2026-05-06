# syntax=docker/dockerfile:1
# Build stage — shell and npm available
FROM ghcr.io/platform-images/nodejs-base:1.0.0 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Runtime stage — no shell, minimal attack surface
FROM ghcr.io/platform-images/nodejs-base:1.0.0-distroless
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
