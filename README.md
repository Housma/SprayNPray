# 🔐 SprayNPray

A simple Python wrapper to automate credential spraying across multiple protocols using [NetExec (nxc)](https://github.com/Pennyw0rth/NetExec).

This tool allows you to provide a list of IP addresses, usernames, and passwords — and attempts authentication over various protocols such as SMB, WinRM, SSH, RDP, LDAP, and MSSQL.

---

## 🚀 Features

- Supports multiple protocols per host
- Brute-force usernames and passwords with NetExec
- Fully customizable command-line arguments
- Easy to modify to include additional NetExec options (e.g. `--shares`, `--local-auth`)

---

## 💻 Requirements

- Python 3
- NetExec (`nxc`) installed and in your `$PATH`
  ```bash
  sudo apt install netexec
  ```

---

## 🧪 Usage

```bash
python3 spraynpray.py  -t targets.txt   -u usernames.txt  -p passwords.txt
```

Where:

- `targets.txt`: one IP per line
- `usernames.txt`: usernames to test
- `passwords.txt`: passwords to test

---

## 🛠️ Example Output

```
[+] Running SMB brute-force against 192.168.1.5 ...
[+] Running WINRM brute-force against 192.168.1.5 ...
[+] Running SSH brute-force against 192.168.1.5 ...
...
```

Any NetExec output (e.g. successful logins) will appear directly in your terminal.

---

## 🔧 Customizing Spray Options

Want to add more NetExec arguments like `--shares` or `--local-auth`?  
Just edit the `run_nxc()` function in `spraynpray.py`.

### Example:

Change this line:

```python
cmd = [
    "nxc", protocol, ip,
    "-u", user_file,
    "-p", pass_file,
    "--continue-on-success"
]
```

To include `--shares`:

```python
cmd = [
    "nxc", protocol, ip,
    "-u", user_file,
    "-p", pass_file,
    "--continue-on-success",
    "--shares"
]
```

Or, make it fully customizable by accepting additional CLI arguments — PRs welcome!

---

## ✅ Supported Protocols

By default, the following protocols are sprayed:

- SMB
- WINRM
- RDP
- SSH
- LDAP
- MSSQL

To change this list, edit the `SUPPORTED_PROTOCOLS` array at the top of the script.

---

