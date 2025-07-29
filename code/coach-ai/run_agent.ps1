# PowerShell script to run the Document Generation Agent
# This script sets up the environment and runs the interactive agent

Write-Host "=== Document Generation Agent Setup ===" -ForegroundColor Green

# Set working directory to the project root
Set-Location $PSScriptRoot

# Load environment variables from secrets.env
Write-Host "Loading environment variables..." -ForegroundColor Yellow
if (Test-Path "secrets.env") {
    Get-Content "secrets.env" | ForEach-Object {
        if ($_ -match '^([^=]+)=(.*)$') {
            [Environment]::SetEnvironmentVariable($matches[1], $matches[2], 'Process')
            Write-Host "  ✓ Loaded $($matches[1])" -ForegroundColor Green
        }
    }
} else {
    Write-Host "  ⚠️  secrets.env not found" -ForegroundColor Yellow
}

# Load environment variables from variables.env
if (Test-Path "variables.env") {
    Get-Content "variables.env" | ForEach-Object {
        if ($_ -match '^([^=]+)=(.*)$') {
            [Environment]::SetEnvironmentVariable($matches[1], $matches[2], 'Process')
            Write-Host "  ✓ Loaded $($matches[1])" -ForegroundColor Green
        }
    }
}

# Enable throttling to avoid rate limits
[Environment]::SetEnvironmentVariable('THROTTLE_LLM_CALLS', '1', 'Process')
Write-Host "  ✓ Enabled LLM call throttling" -ForegroundColor Green

Write-Host "`nStarting Document Generation Agent...`n" -ForegroundColor Green

# Run the agent
try {
    python -m docgen_agent
} catch {
    Write-Host "Error running the agent: $_"
    Write-Host "Make sure you have installed the requirements: pip install -r requirements.txt"
    pause
}
