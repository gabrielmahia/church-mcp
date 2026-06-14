# AI-KungFU East Africa MCP Server
# Glama-compatible Dockerfile for church-mcp
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/church-mcp"
LABEL org.opencontainers.image.description="church-mcp — East Africa AI Coordination Infrastructure"
LABEL org.opencontainers.image.licenses="MIT"

RUN pip install --no-cache-dir church-mcp

CMD ["church-mcp"]
