# Shadow313 v2

**Local-First AI-Powered Security Intelligence CLI**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modular, offline-capable, AI-augmented security intelligence command-line interface that runs entirely on your machine — no telemetry, no data exfiltration, no cloud dependency required.

## Features

- **28 Modules** spanning reconnaissance, vulnerability intelligence, exploit advisory, network forensics, defense hardening, quantum cryptography migration, and agentic automation
- **Local-First AI** — All inference via Ollama by default (localhost:11434)
- **Privacy-Preserving** — AES-256-GCM encrypted sessions, zero telemetry
- **Modular Architecture** — Each capability is a self-contained Python package
- **Advisory-Safe** — Exploitation features require explicit `--lab-mode` flag and `scope.yaml` authorization

## Quick Start

```bash
# Install
pip install shadow313

# Run a recon scan
shadow313 recon --target example.com --mode full

# Vulnerability analysis
shadow313 vuln --target example.com

# Network intelligence
shadow313 network --interface eth0 --mode monitor
```

## Architecture

```
┌─────────────────────────────────────────┐
│           CLI INTERFACE                 │
│    (argparse → command bus dispatch)    │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│           CORE KERNEL                   │
│  (config, session, AI engine, output)   │
└──────────────┬──────────────────────────┘
               │
    ┌──────────┼──────────┐
    │          │          │
┌───▼───┐  ┌──▼───┐  ┌──▼───┐
│ Recon │  │ Vuln │  │ Net  │  ... 28 modules
└───────┘  └──────┘  └──────┘
```

## Modules

### V1 Core (9 modules)
1. **Core Kernel** — Command bus, session management, AI engine
2. **Recon** — OSINT, DNS, subdomain enumeration
3. **Vulnerability Analysis** — CVE matching, EPSS scoring
4. **Exploit Advisory** — Lab-safe exploit recommendations
5. **Network Intelligence** — Packet analysis, TLS fingerprinting
6. **Defense & Hardening** — Configuration audits, CIS benchmarks
7. **Quantum Cryptography** — Post-quantum migration assessment
8. **Plugin System** — YAML manifests, sandboxed execution
9. **CI/CD Integration** — GitHub Actions, GitLab CI templates

### V2 Advanced (19 features)
- **AI/RAG/Agentic** — RAG knowledge base, auto-chain loops
- **Vuln Intelligence** — EPSS, CISA KEV, MITRE ATT&CK
- **Network Upgrades** — ML anomaly detection, JA3/JA3S, DNS covert channels
- **Campaign Platform** — Campaign manager, intelligence graph, web dashboard, PDF reports
- **Security & Trust** — Encrypted sessions, plugin code signing, threat intel feeds
- **Advanced Capabilities** — Docker CVE reproducer, Cloud/K8s/IaC hardening, crypto agility

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.11+ |
| AI Backend | Ollama (local) / OpenAI-compatible |
| Vector Store | ChromaDB + TF-IDF fallback |
| Database | SQLite (stdlib) |
| Graph Engine | NetworkX + pure-Python fallback |
| ML Anomaly | scikit-learn IsolationForest |
| Web Dashboard | FastAPI + HTMX (port 7313) |
| PDF Reports | Jinja2 + WeasyPrint |

## Privacy & Security

- **Zero telemetry** — No analytics, no phone-home
- **Encrypted sessions** — AES-256-GCM in `~/.shadow313/sessions/`
- **Lab-safe exploitation** — Requires `--lab-mode` + `scope.yaml`
- **Local AI** — Ollama runs on localhost:11434 by default

## Documentation

- [Module Design Document](docs/DESIGN.md)
- [CLI Command Reference](docs/CLI_REFERENCE.md)
- [Security Glossary](docs/GLOSSARY.md)
- [Plugin Development Guide](docs/PLUGINS.md)

## License

MIT © 2026 Shadow313
