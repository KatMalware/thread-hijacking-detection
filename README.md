# thread-hijacking-detection


Linux Threat Monitor is a lightweight security monitoring toolkit for Linux that uses eBPF/BPFtrace to detect high-risk runtime behaviors such as `ptrace()` abuse (process hijacking), `clone()` misuse (suspicious thread/process creation), and write-to-executable memory operations (shellcode or exploit activity). The project includes standalone eBPF detectors, a Python-based correlation engine that aggregates events and assigns risk scores to processes in real time, and small test programs to simulate attacks. Designed for research, education, and SOC labs, the toolkit provides a simple, modular, and extensible foundation for building behavioral threat detection without kernel modules, heavy agents, or complex infrastructure.

---

## ✨ Features

- Real-time detection of security-sensitive syscalls  
- Behavior correlation and process-level risk scoring  
- Lightweight eBPF/BPFtrace agents  
- Pure userspace correlation engine (Python)  
- Test programs to simulate malicious behavior  
- Modular design for easy extension  

---

## 🧱 System Requirements

- Linux with eBPF support  
- `bpftrace` installed  
- Python 3.8+  
- root privileges  

---

## 📥 Installation

Install bpftrace:

```bash
sudo apt install bpftrace
# or
sudo dnf install bpftrace
# or
yay -S bpftrace

#Install Python dependencies:
pip install -r requirements.txt

#Running Detectors
sudo bpftrace bpf/detect_ptrace.bt
sudo bpftrace bpf/detect_clone.bt
sudo bpftrace bpf/detect_write_exec.bt

#Run Event Correlator
python3 src/monitor.py

#Testing Detection
cd tests/
gcc test_ptrace.c -o ptrace_test
gcc test_clone.c -o clone_test
gcc test_write_exec.c -o we_test -z execstack

#Run them:
./ptrace_test
./clone_test
./we_test

#Sample Output
=== Threat Scores ===
[!] attacker: 9 (suspicious)
[*] sshd: 2
[*] bash: 1


#Architecture
    Kernel Events
        |
    eBPF/BPFtrace
        |
   Event Streams
        |
+--------------------+
| Python Correlator  |
| - Parse events     |
| - Risk scoring     |
| - Reporting        |
+--------------------+
        |
 Real-Time Alerts



