import os
import subprocess
import sys

ENV_NAME = "vngoc_hkt"
REQ_FILE = "requirements.txt"

def run(cmd):
    print(f"\n▶ {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def create_venv():
    print("Creating virtual environment...")
    run(f"{sys.executable} -m venv {ENV_NAME}")

def pip_path():
    return os.path.join(ENV_NAME, "bin", "pip")

def python_path():
    return os.path.join(ENV_NAME, "bin", "python")

def install_requirements():
    pip = pip_path()

    # upgrade pip tools (IMPORTANT FIX for Linux errors)
    run(f"{pip} install --upgrade pip setuptools wheel")

    # install dependencies
    run(f"{pip} install -r {REQ_FILE}")

def install_jupyter_kernel():
    python = python_path()

    run(f"{python} -m pip install ipykernel")
    run(f"{python} -m ipykernel install --user --name={ENV_NAME} --display-name '{ENV_NAME}'")

def main():
    create_venv()
    install_requirements()
    install_jupyter_kernel()

    print("\n✅ ENV SETUP DONE SUCCESSFULLY!")
    print(f"Activate with: source {ENV_NAME}/bin/activate")

if __name__ == "__main__":
    main()
