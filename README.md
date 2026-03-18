# pymatlab

Python scripts to connect to and control MATLAB via the MATLAB Engine API for Python.

## Contents

| File | Description |
|:-----|:------------|
| `test_matlab_engine.py` | Example script demonstrating MATLAB engine connection and usage |
| `install_matlab_engine.ps1` | PowerShell script to install the MATLAB Engine API for Python |

## Setup

1. Install MATLAB Engine API for Python:
   ```powershell
   # Windows (PowerShell)
   .\install_matlab_engine.ps1
   ```
   Or manually:
   ```bash
   cd "matlabroot/extern/engines/python"
   python setup.py install
   ```

2. Test the connection:
   ```bash
   python test_matlab_engine.py
   ```

## Requirements

- MATLAB (with Engine API for Python support)
- Python 3.x
