# AetheroOS Forgejo Sovereign Git Backend

This directory contains the setup for a self-hosted Forgejo instance to serve as the sovereign Git backend for AetheroOS architecture.

## Quick Start

```bash
cd forgejo
./start_forgejo.sh
```

## What's Included

- **docker-compose.yml**: Complete Forgejo setup with persistent storage
- **start_forgejo.sh**: Helper script to launch and manage the instance

## Features

- 🔒 **Sovereign Control**: Full ownership of your Git infrastructure
- 🐳 **Docker-based**: Easy deployment and management
- 🔄 **Persistent Data**: All repositories and settings are preserved
- 🌐 **Web Interface**: Available at http://localhost:3000
- 🔑 **SSH Access**: Git operations via ssh://git@localhost:222
- 🛡️ **User Isolation**: Runs with UID/GID 1000 for security

## Management Commands

```bash
# Start services
./start_forgejo.sh

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Update to latest version
docker-compose pull && docker-compose up -d

# Restart services
docker-compose restart
```

## Initial Setup

1. Run `./start_forgejo.sh`
2. Visit http://localhost:3000
3. Complete the installation wizard
4. Create your admin account
5. Start creating repositories for AetheroOS components

## Integration with AetheroOS

Once running, you can:
- Host all Aethero repositories locally
- Set up CI/CD pipelines
- Manage team access and permissions
- Create webhooks for automated deployments
- Mirror external repositories

## Data Persistence

All data is stored in the `forgejo_data` Docker volume, ensuring your repositories and configuration survive container restarts and updates.
