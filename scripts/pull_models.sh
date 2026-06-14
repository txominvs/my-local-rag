#!/bin/bash
docker exec my-local-rag-ollama-1 ollama pull nomic-embed-text
docker exec my-local-rag-ollama-1 ollama pull llama3.2:1b