import subprocess
import sys
import os
import time

def main():
    print("Starting RIMLang Interpreter...")
    print("Backend: http://127.0.0.1:5000")
    print("Frontend: http://localhost:5173")
    print("Press Ctrl+C to stop")
    print("-" * 50)
    

    backend_process = subprocess.Popen([sys.executable, "app.py"], cwd="backend")
    
    time.sleep(2)
    
    frontend_process = subprocess.Popen(["npm", "run", "dev"], cwd="frontend/app")
    
    try:
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        backend_process.terminate()
        frontend_process.terminate()
        print("Servers stopped.")

if __name__ == "__main__":
    main()