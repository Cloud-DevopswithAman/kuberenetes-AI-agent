# API Specification

## Overview

The backend exposes a compact set of endpoints for cluster investigation, progress tracking, and history.

## Endpoints

### Health check

GET /health

Response:

```json
{
  "status": "ok"
}
```

### List clusters

GET /clusters

Response:

```json
{
  "clusters": ["minikube", "docker-desktop", "kind-kind"],
  "current_context": "docker-desktop",
  "kubeconfig": "C:\\Users\\User\\.kube\\config"
}
```

### Start investigation

POST /investigate

Request body:

```json
{
  "namespace": "default",
  "context": "docker-desktop"
}
```

Response:

```json
{
  "status": "success",
  "investigation_id": "uuid",
  "context": "docker-desktop",
  "investigation": {
    "progress_id": "uuid",
    "pods": {"healthy": true, ...},
    "logs": {"status": "collected", ...},
    "events": {"status": "analyzed", ...},
    "deployments": {"status": "inspected", ...},
    "network": {"status": "inspected", ...}
  },
  "diagnosis": {
    "root_cause": "Pod is failing due to ImagePullBackOff",
    "explanation": "The pod cannot start because the image registry is unreachable.",
    "fix": "Verify container image name and registry credentials.",
    "kubectl_command": "kubectl describe pod <pod-name> -n default",
    "confidence": 72
  }
}
```

### Progress polling

GET /progress/{progress_id}

Response:

```json
{
  "progress": {
    "steps": [
      {"name": "Checking Pods", "status": "completed"},
      {"name": "Reading Logs", "status": "completed"},
      {"name": "AI Reasoning", "status": "running"}
    ],
    "completed": false
  }
}
```

### Investigation history

GET /history

Response:

```json
{
  "history": [
    {
      "timestamp": "2026-06-27T12:34:56Z",
      "user": "admin",
      "namespace": "default",
      "context": "docker-desktop",
      "root_cause": "CrashLoopBackOff due to failed image pull",
      "confidence": 72,
      "status": "completed"
    }
  ]
}
```

## Notes

- Investigation requests are read-only and cluster-aware.
- Secrets and sensitive data should be omitted from outputs.
- History records include selected kubeconfig context for auditability.
