# syntax=docker/dockerfile:1
# Build stage — Maven available
FROM ghcr.io/platform-base-images/openjdk-base:1.0.23@sha256:0a33c6483a4b4445b327ed13fff26d02fc842066c823371dd0c8decc9d83f8b7 AS builder
USER root
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -q
COPY src/ ./src/
RUN mvn package -DskipTests -q
USER nonroot

# Runtime stage — no shell, no Maven
FROM ghcr.io/platform-base-images/openjdk-base:1.0.23-distroless@sha256:918c93230f14beec124d448db0d32918c100f2c11a26a4161a22ddd8be981fb2
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
