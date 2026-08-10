# syntax=docker/dockerfile:1
# Build stage — Maven available
FROM ghcr.io/platform-base-images/openjdk-base:1.0.22@sha256:d825fb250dc3e505e8898de3842bcc85edd940130a3bf4b0f3b250b1533f023d AS builder
USER root
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -q
COPY src/ ./src/
RUN mvn package -DskipTests -q
USER nonroot

# Runtime stage — no shell, no Maven
FROM ghcr.io/platform-base-images/openjdk-base:1.0.22-distroless
ARG BUILD_DATE
ARG GIT_REVISION
LABEL org.opencontainers.image.source="https://github.com/platform-base-images/app-reference-implementations"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.created="${BUILD_DATE}"
LABEL org.opencontainers.image.revision="${GIT_REVISION}"
WORKDIR /app
COPY --from=builder /app/target/java-api-1.0.0.jar app.jar
EXPOSE 8080
CMD ["-jar", "/app/app.jar"]
