FROM dart:latest AS builder

WORKDIR /app

COPY main.dart .
RUN dart compile exe main.dart

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/main.dart .
CMD ["dart", "main.dart"]