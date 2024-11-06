import os
import subprocess
import sys

def create_virtualenv(venv_dir):
    """
    creates a virtual environment.
    """
    print("Creating virtual environment...")
    subprocess.check_call([sys.executable, "-m", "blvkmvn_music", venv_dir])
    print(f"Virtual environment created at: {venv_dir}")

def install_requirements(venv_dir):
    """
    Install required packages from requirements.txt.
    """
    requirements_file = "requirements.txt"
    pip_executable = os.path.join(venv_dir, "bin", "pip") 
    print("Installing requirements...")
    subprocess.check_call([pip_executable, "install", "-r", requirements_file])
    print("Requirements installed.")

def make_program_global(script_name):
    """
    Create a symbolic link to make the program globally accessible.
    """
    script_path = os.path.abspath(script_name)
    bin_dir = os.path.join(os.path.expanduser("~"), ".local", "bin")  
    os.makedirs(bin_dir, exist_ok=True)
    symlink_path = os.path.join(bin_dir, script_name)

    # Create symbolic link
    if os.path.exists(symlink_path):
        print(f"Removing existing symlink: {symlink_path}")
        os.remove(symlink_path)
    
    print(f"Creating symlink: {symlink_path} -> {script_path}")
    os.symlink(script_path, symlink_path)
    print("Program is now globally accessible.")

def main():
    venv_dir = "venv"  # Directory for the virtual environment
    script_name = "musicx.py"  # the main script

    create_virtualenv(venv_dir)
    install_requirements(venv_dir)
    make_program_global(script_name)

if __name__ == "__main__":
    main()