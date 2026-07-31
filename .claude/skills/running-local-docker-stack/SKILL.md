---
name: running-local-docker-stack
description: Discover, start, rebuild, migrate, diagnose, and verify a repository's local Docker Compose stack without assuming service names, ports, environment files, or project-specific topology. Use for local container stack operations and readiness checks.
---

# Running a Local Docker Stack

Discover the stack before mutating it. Never reuse instructions from another repository.

## 1. Inspect

Read the project contract and container docs, then locate Compose files, overrides, profiles, Dockerfiles, environment templates, health checks, volumes, migration jobs, and package scripts. Use `docker compose config --services`, `--profiles`, and `docker compose ps -a` where supported.

Do not print resolved secrets from `docker compose config`. Do not read or create real `.env` files without explicit permission; work from committed examples and report missing variable names only.

## 2. Choose the smallest action

- Already healthy: verify only.
- Configuration-only change: recreate affected services.
- Source/Dockerfile/dependency change: build only affected images.
- Schema change: run the repository's documented migration job before or during startup as documented.
- First start: pull/build and start dependencies in their required order.

Before starting, check occupied host ports, existing project names/containers, required networks, disk capacity, and whether destructive volume recreation is actually necessary. Never add `-v`, delete volumes, or reset databases without explicit confirmation and a recovery plan.

## 3. Start and observe

Use the repository's documented command when present; otherwise compose a minimal `docker compose up -d` command with the discovered files/profiles/services. Avoid rebuilding everything by default.

Watch service state and health until each required service is healthy, exited successfully as a job, or failed with useful logs. Diagnose the first causal failure rather than cascading dependency errors.

## 4. Verify at two levels

1. Shallow: expected containers, health status, ports, migration exit status, absence of restart loops.
2. Deep: one real local end-to-end action through the public entrypoint, chosen from project docs or acceptance criteria.

Report commands, Compose files/profiles, reachable URLs, unhealthy services, relevant masked log excerpts, and exact stop/restart instructions. Do not leave attached log streams or temporary containers running unintentionally.
