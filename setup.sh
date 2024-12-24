#!/bin/bash

# Set variables
REPO_URL="https://github.com/DDidas/DLRG.git"
REPO_DIR="$HOME/DLRG"
DESKTOP_FILE="$HOME/Desktop/DLRG_Start.desktop"
ENTRY_SCRIPT="$REPO_DIR/start_uvicorn.sh"

echo "### DLRG Setup Script ###"

# Clone the repository
if [ ! -d "$REPO_DIR" ]; then
    echo "Cloning repository..."
    git clone "$REPO_URL" "$REPO_DIR"
else
    echo "Repository already cloned."
fi

# Navigate to the repository directory
cd "$REPO_DIR" || { echo "Failed to navigate to $REPO_DIR"; exit 1; }

# Install dependencies
echo "Installing Python and Node.js dependencies..."
pip install eel uvicorn --user
npm install

# Create the start script
echo "Creating Uvicorn start script..."
cat <<EOF > "$ENTRY_SCRIPT"
#!/bin/bash
cd "$REPO_DIR"
uvicorn main:api --reload
EOF
chmod +x "$ENTRY_SCRIPT"

# Create the desktop entry
echo "Creating desktop entry..."
cat <<EOF > "$DESKTOP_FILE"
[Desktop Entry]
Version=1.0
Type=Application
Name=DLRG API Starter
Exec=bash -c '$ENTRY_SCRIPT'
Icon=utilities-terminal
Terminal=true
EOF
chmod +x "$DESKTOP_FILE"

echo "Setup complete! Double-click the 'DLRG API Starter' icon on your Desktop to start Uvicorn."
