# syntax=docker/dockerfile:1
# Build stage — Maven available
FROM ghcr.io/platform-base-images/openjdk-base:1.0.36@sha256:be22f9be5c1e8b9d84c670fb74655833dd63339ab2fb9e6adc7ca3257106d75a AS builder
USER root
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -q
COPY src/ ./src/
RUN mvn package -DskipTests -q
USER nonroot

# Runtime stage — no shell, no Maven
FROM ghcr.io/platform-base-images/openjdk-base:1.0.36-distroless@sha256:e9176c8f2de627354b6d68b0c9c8a4863f15cd8f935929acd5cc4d91a360d18b
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
