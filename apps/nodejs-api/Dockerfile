# syntax=docker/dockerfile:1
# Build stage — shell and npm available
FROM ghcr.io/platform-base-images/nodejs-base:1.0.24@sha256:d586c209ac52aeff8e1e8628613d03eed540c1868d02aca19a665c4e6d97d39a AS builder
USER root
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
USER nonroot

# Runtime stage — nodejs-base has no distroless variant currently (Chainguard's
# distroless node image was stuck on an unpatched libnghttp2/npm with no shell to
# work around it; see platform-base-images/hardened-base). Using the standard
# variant here instead.
FROM ghcr.io/platform-base-images/nodejs-base:1.0.24@sha256:d586c209ac52aeff8e1e8628613d03eed540c1868d02aca19a665c4e6d97d39a
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
CMD ["node", "src/index.js"]
