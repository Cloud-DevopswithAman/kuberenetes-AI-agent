# Implementation Plan

## Phase 1 - Foundation

### Objectives

- create the backend service
- create a simple frontend trigger
- connect to a Kubernetes cluster using kubeconfig
- implement a basic investigation workflow

### Deliverables

- FastAPI app with health endpoint
- endpoint to start an investigation request
- Kubernetes client integration
- simple JSON response with cluster evidence

## Phase 2 - Investigation capabilities

### Objectives

- collect pod health, deployment health, and recent events
- inspect service and ingress state
- collect logs from failing pods

### Deliverables

- investigation module for pod and deployment inspection
- log collection helper
- evidence summarizer

## Phase 3 - AI reasoning integration

### Objectives

- send the investigation summary to the LLM
- produce root cause and remediation suggestions
- return structured output to the frontend

### Deliverables

- LLM prompt template
- response parser
- diagnosis schema with fields such as:
  - summary
  - rootCause
  - evidence
  - suggestedFix
  - confidence
  - nextSteps

## Phase 4 - UI refinement

### Objectives

- present diagnosis clearly to the user
- show evidence and recommended actions
- add loading and error states

### Deliverables

- investigation results page
- status cards
- expandable evidence view

## Phase 5 - Production hardening

### Objectives

- add auditing
- add rate limiting
- add authentication
- improve observability and error handling

### Deliverables

- logging and metrics
- secure secret management
- role-based access control
- investigation history storage

## Suggested milestone order

1. Create FastAPI skeleton
2. Connect to Kubernetes cluster
3. Build evidence collection
4. Add LLM reasoning
5. Add frontend display
6. Harden for production

## Recommended first sprint

The first sprint should focus only on:
- one namespace inspection flow
- pod and deployment status checks
- event and log collection
- a single diagnosis response

This keeps the project narrow and valuable without introducing operator complexity.
