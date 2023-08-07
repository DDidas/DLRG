const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

function startFastAPI() {
    // Replace "/usr/local/bin/npm" with the absolute path of npm on your system
    const npmPath = "/usr/local/bin/npm";

    // Spawn the FastAPI server process using the absolute path of npm
    const fastAPIProcess = spawn(npmPath, ['run', 'start-fastapi']);

    // Handle FastAPI process events
    fastAPIProcess.stdout.on('data', (data) => {
        console.log(`FastAPI stdout: ${data}`);
    });

    fastAPIProcess.stderr.on('data', (data) => {
        console.error(`FastAPI stderr: ${data}`);
    });

    fastAPIProcess.on('close', (code) => {
        console.log(`FastAPI process exited with code ${code}`);
    });
}

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        fullscreen: true, // Set fullscreen to true
    });

    mainWindow.loadFile(path.join(__dirname, 'frontend/html', 'login_page.html'));
}

app.whenReady().then(() => {
    createWindow();
    startFastAPI();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
