# API Specification

## Overview

The backend exposes a small set of endpoints for starting investigations and checking service health.

## Endpoints

### Health check

GET /health

Response:

```json
{
  "status": "ok"
}
```

### Start investigation

POST /investigate

Request body:

```json
{
  "namespace": "default",
  "resourceType": "deployment",
  "resourceName": "my-app"
}
```

Response:

```json
{
  "requestId": "uuid",
  "status": "completed",
  "summary": "Pod crash loops detected",
  "rootCause": "Image pull failure caused by invalid registry credentials",
  "evidence": [
    "Pod is in CrashLoopBackOff",
    "Recent events show ImagePullBackOff"
  ],
  "suggestedFix": [
    "Verify image pull secret",
    "Check registry credentials"
  ],
  "confidence": "high",
  "nextSteps": [
    "Inspect secret and image reference"
  ]
}
```

### Investigation history

GET /history

Response:

```json
{
  "investigations": []
}
```

## Notes

- The first version should be read-only.
- All investigation requests should be logged for auditability.
- Avoid returning secrets from cluster inspection output.
