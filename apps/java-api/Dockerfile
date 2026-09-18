# syntax=docker/dockerfile:1
# Build stage — Maven available
FROM ghcr.io/platform-base-images/openjdk-base:1.0.31@sha256:72e387ce3b124ff4fe5be3133da1f6bfc4fc2559f9254b30fff1fa4a7d8adc4b AS builder
USER root
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -q
COPY src/ ./src/
RUN mvn package -DskipTests -q
USER nonroot

# Runtime stage — no shell, no Maven
FROM ghcr.io/platform-base-images/openjdk-base:1.0.31-distroless@sha256:532967f7f089fa646a53a6e8cbc64b7d3d4d395cc629fe76c944ab4286155d4f
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
