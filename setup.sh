#!/bin/bash

# Set variables
REPO_URL="https://github.com/DDidas/DLRG.git"
REPO_DIR="$HOME/DLRG"
DESKTOP_FILE="$HOME/Desktop/DLRG_Start.desktop"
ENTRY_SCRIPT="$REPO_DIR/start_uvicorn.sh"
VENV_DIR="$REPO_DIR/venv"

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

# Create a virtual environment for Python
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Install Python dependencies
echo "Installing Python dependencies..."
pip install eel uvicorn --upgrade

# Install Node.js dependencies
echo "Installing Node.js dependencies..."
npm install

# Create the start script
echo "Creating Uvicorn start script..."
cat <<EOF > "$ENTRY_SCRIPT"
#!/bin/bash
cd "$REPO_DIR"
source "$VENV_DIR/bin/activate"
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
