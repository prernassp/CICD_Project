#!/bin/bash

# Variables
REPO_URL="https://github.com/prernassp/CICD_Project.git"
DEST_DIR="/home/ubuntu/CICD_Project/"

# Pull the latest code
echo "Pulling the latest code from $REPO_URL..."
if [ -d "$DEST_DIR/.git" ]; then
  cd "$DEST_DIR" && git pull origin main
else
  git clone "$REPO_URL" "$DEST_DIR"
fi
sudo mv /home/ubuntu/CICD_Project/project.html /var/www/html/index.html
# Restart Nginx
echo "Restarting Nginx..."
sudo systemctl restart nginx

# Verify the restart
if systemctl is-active --quiet nginx; then
  echo "Nginx restarted successfully."
else
  echo "Failed to restart Nginx." >&2
  exit 1
fi

echo "Deployment complete."
