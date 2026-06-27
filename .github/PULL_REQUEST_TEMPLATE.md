## Summary

Describe the main change in this PR and why it matters.

## What changed

- Added docs, CI workflow, and repo preview assets.
- Added cluster context selection support.
- Updated README with badges and run instructions.

## How to verify

1. Pull the branch.
2. Run `docker compose up --build`.
3. Confirm the frontend loads and the backend health endpoint is reachable.

## Notes

- This PR is read-only for Kubernetes investigation.
- The repo includes a helper compose file for mounting host kubeconfig.
