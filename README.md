# Feature Store Serving Sim

TypeScript simulation of online feature serving, latency-aware lookups, and fallback behavior.

## Why This Exists

Framed like a serving-layer prototype for ML platform teams that care about low-latency retrieval and operational fallbacks.

## What This Demonstrates

- online-serving style request handling
- fallback and latency-aware decision logic
- compact codebase with real platform flavor

## Architecture

1. entity requests are mapped to feature retrieval plans
1. serving logic resolves primary and fallback sources
1. results summarize feature freshness and serving posture

## Run It

```bash
npm test
npm run build
```

## Verification

Run `npm test` and `npm run build` to validate serving behavior.
