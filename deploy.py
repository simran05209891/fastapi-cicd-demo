import os
import subprocess
from datetime import datetime

def run_command(command):
    print(f"\n🔹 Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
    else:
        print(f"✅ Output: {result.stdout}")

def deploy():
    print("🚀 Starting Deployment...")
    print(f"🕒 Time: {datetime.now()}")

    # Go to project directory
    os.chdir("/home/whizcamp/project")

    # Pull latest code
    run_command("git pull origin main")

    # Stop existing containers
    run_command("docker-compose down")

    # Build & start containers
    run_command("docker-compose up -d --build")

    print("\n🎉 Deployment Completed Successfully!")

if __name__ == "__main__":
    deploy()
