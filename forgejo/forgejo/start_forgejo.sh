#!/bin/bash
# AetheroOS Forgejo Sovereign Git Backend Launcher
# Compatible with macOS and Linux

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 AetheroOS Forgejo Sovereign Backend${NC}"
echo -e "${BLUE}======================================${NC}"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo -e "${RED}❌ Docker is not running. Please start Docker and try again.${NC}"
    exit 1
fi

# Check if Docker Compose is available
if ! command -v docker-compose > /dev/null 2>&1 && ! docker compose version > /dev/null 2>&1; then
    echo -e "${RED}❌ Docker Compose is not available. Please install Docker Compose.${NC}"
    exit 1
fi

# Navigate to forgejo directory
cd "$(dirname "$0")"

echo -e "${YELLOW}📦 Pulling latest Forgejo image...${NC}"
docker-compose pull

echo -e "${YELLOW}🔧 Starting Forgejo services...${NC}"
docker-compose up -d

# Wait for service to be ready
echo -e "${YELLOW}⏳ Waiting for Forgejo to initialize...${NC}"
sleep 10

# Check if service is running
if docker-compose ps | grep -q "Up"; then
    echo -e "${GREEN}✅ Forgejo is now running!${NC}"
    echo -e "${GREEN}🌐 Web Interface: http://localhost:3000${NC}"
    echo -e "${GREEN}🔑 SSH Git Access: ssh://git@localhost:222${NC}"
    echo ""
    echo -e "${BLUE}📋 First-time setup:${NC}"
    echo -e "   1. Visit http://localhost:3000"
    echo -e "   2. Complete the initial configuration"
    echo -e "   3. Create your admin account"
    echo -e "   4. Start using your sovereign Git backend!"
    echo ""
    echo -e "${BLUE}🛠️ Management commands:${NC}"
    echo -e "   Stop:    docker-compose down"
    echo -e "   Restart: docker-compose restart"
    echo -e "   Logs:    docker-compose logs -f"
    echo -e "   Update:  docker-compose pull && docker-compose up -d"
else
    echo -e "${RED}❌ Failed to start Forgejo. Check logs with: docker-compose logs${NC}"
    exit 1
fi
