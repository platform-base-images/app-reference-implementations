# syntax=docker/dockerfile:1
# Build stage — Maven available
FROM ghcr.io/platform-base-images/openjdk-base:1.0.28@sha256:561cb316cd098cac473115425e8329dc6b87cf2bf452947ad27096128516ead7 AS builder
USER root
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -q
COPY src/ ./src/
RUN mvn package -DskipTests -q
USER nonroot

# Runtime stage — no shell, no Maven
FROM ghcr.io/platform-base-images/openjdk-base:1.0.28-distroless@sha256:9a356c5fc607bfed756253351da6048a2548a377452f21b00d5da1db814ebfe3
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
