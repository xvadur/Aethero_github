#!/bin/bash

# 🕷️ AetheroOS Spider-Man Dashboard Deploy Script
# Prepares Spider-Man themed dashboard for Vercel deployment and pushes to GitHub

echo "🕷️ Preparing AetheroOS Spider-Man Dashboard for Vercel deployment..."

# 1. Ensure public directory exists
mkdir -p dashboard/public

# 2. Copy any new HTML/CSS/JS files to public (if they exist in dashboard root)
mv dashboard/*.html dashboard/*.css dashboard/*.js dashboard/public/ 2>/dev/null || true

# 3. Verify vercel.json configuration
if [ ! -f "dashboard/vercel.json" ]; then
    echo "📝 Creating vercel.json..."
    cat > dashboard/vercel.json <<EOF
{
  "outputDirectory": "public",
  "buildCommand": "npm run build",
  "framework": "other"
}
EOF
fi

# 4. Verify package.json configuration
if [ ! -f "dashboard/package.json" ]; then
    echo "📝 Creating package.json..."
    cat > dashboard/package.json <<EOF
{
  "name": "aethero-dashboard",
  "version": "1.0.0",
  "description": "AetheroOS Introspective Dashboard",
  "scripts": {
    "dev": "python -m http.server 3000",
    "build": "echo 'Static files ready for deployment'",
    "start": "python -m http.server 8080"
  },
  "author": "AetheroOS",
  "license": "MIT"
}
EOF
fi

# 5. Git operations
echo "📦 Committing and pushing changes..."
git add .
git commit -m "Dashboard update: $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main

echo "✅ Dashboard deployed! Check https://vercel.com/xvadurs-projects/aethero-github for build status."
echo "🌐 Your dashboard will be available at the Vercel URL once deployment completes."
