import subprocess


def shutdown_system():
    subprocess.run(["sudo", "shutdown", "-h", "now"], check=True)
