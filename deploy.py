import os
import subprocess
import time
from datetime import datetime

def run_command(command):
    print(f"\n🔹 Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Error:\n{result.stderr}")
        exit(1)
    else:
        print(f"✅ Success:\n{result.stdout}")

def health_check():
    print("\n🔍 Running Health Check...")
    time.sleep(5)  # wait for container to start
    
    response = subprocess.run("curl -s http://localhost", shell=True, capture_output=True, text=True)
    
    if "message" in response.stdout:
        print("✅ Application is LIVE and working!")
    else:
        print("❌ Health check failed!")
        exit(1)

def deploy():
    print("🚀 Starting Deployment...")
    print(f"🕒 Time: {datetime.now()}")

    os.chdir("/home/whizcamp/project")

    # Step 1: Pull latest code
    run_command("git pull origin main")

    # Step 2: Stop old containers
    run_command("docker-compose down")

    # Step 3: Build & deploy
    run_command("docker-compose up -d --build")

    # Step 4: Health check
    health_check()

    print("\n🎉 Deployment Completed Successfully!")

if __name__ == "__main__":
    deploy()
