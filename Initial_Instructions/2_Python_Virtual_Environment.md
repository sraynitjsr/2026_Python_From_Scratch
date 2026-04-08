# 🐍 Python Virtual Environments (venv)

## What is a Virtual Environment?

A **virtual environment** is an isolated Python workspace that keeps your project dependencies separate from other projects and your system Python installation.

Think of it like having separate toolboxes for different projects - each toolbox has exactly the tools (packages) you need for that specific project, without mixing them up.

---

## 🤔 Why Do We Need Virtual Environments?

### The Problem Without Virtual Environments:

Imagine you're working on two projects:

**Project A:** Needs Django version 3.2  
**Project B:** Needs Django version 4.2  

**Without virtual environments:**
- You can only have ONE version of Django installed globally
- Installing Django 4.2 will overwrite Django 3.2
- Project A breaks! 💥

**With virtual environments:**
- Project A has its own isolated environment with Django 3.2
- Project B has its own isolated environment with Django 4.2
- Both projects work perfectly! ✅

---

## 🎯 Key Benefits

1. **Dependency Isolation** - Each project has its own packages
2. **Version Control** - Different versions of the same package in different projects
3. **Clean System** - Keeps your global Python installation clean
4. **Reproducibility** - Easy to share exact dependencies with others
5. **No Permission Issues** - No need for sudo/admin rights to install packages

---

## 📦 Creating a Virtual Environment

### Step 1: Check Python Installation

```bash
python3 --version
```

**Output:**
```
Python 3.13.3
```

You should have Python 3.3+ (venv is built-in).

---

### Step 2: Create a Virtual Environment

**Syntax:**
```bash
python3 -m venv <environment_name>
```

**Common names:** `venv`, `env`, `.venv`, `virtualenv`

**Example:**
```bash
python3 -m venv myenv
```

**What happens:**
- Creates a folder named `myenv` in your current directory
- Contains a copy of Python interpreter
- Contains pip (package manager)
- Contains space for installed packages

**Folder structure created:**
```
myenv/
├── bin/           # Executables (Mac/Linux)
│   ├── python3
│   ├── pip
│   └── activate
├── include/       # C headers
├── lib/           # Installed packages go here
│   └── python3.13/
│       └── site-packages/
└── pyvenv.cfg     # Configuration
```

---

## 🚀 Activating the Virtual Environment

You must **activate** the virtual environment before using it.

### On macOS/Linux:

```bash
source myenv/bin/activate
```

### On Windows:

```bash
myenv\Scripts\activate
```

### What Happens When Activated:

**Before activation:**
```bash
$ which python3
/opt/homebrew/bin/python3
```

**After activation:**
```bash
(myenv) $ which python3
/Users/yourname/project/myenv/bin/python3
```

**Notice:**
- Your prompt now shows `(myenv)` - you're in the virtual environment!
- `python3` now points to the virtual environment's Python
- Any packages you install go into `myenv/lib/python3.13/site-packages/`

---

## 📥 Installing Packages in Virtual Environment

Once activated, use `pip` to install packages:

```bash
(myenv) $ pip install requests
```

**What happens:**
- Installs `requests` library INTO the virtual environment
- Only available when this environment is activated
- Does NOT affect your global Python installation

### Check Installed Packages:

```bash
(myenv) $ pip list
```

**Output:**
```
Package    Version
---------- -------
pip        24.0
requests   2.31.0
```

---

## 🛑 Deactivating the Virtual Environment

When you're done working, deactivate the environment:

```bash
(myenv) $ deactivate
```

**What happens:**
- Prompt returns to normal (no more `(myenv)`)
- Shell uses system Python again
- Virtual environment packages are no longer accessible

You can reactivate anytime with `source myenv/bin/activate`

---

## 📋 Complete Workflow Example

### Creating a New Project:

```bash
# 1. Create project folder
mkdir my_project
cd my_project

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate

# 4. Install packages
pip install requests pandas

# 5. Work on your project
python3 main.py

# 6. When done
deactivate
```

---

## 📝 Requirements File (requirements.txt)

### What is it?

A text file listing all packages and versions your project needs.

### Creating requirements.txt:

```bash
(venv) $ pip freeze > requirements.txt
```

**File content (requirements.txt):**
```
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.7
numpy==1.26.4
pandas==2.2.1
python-dateutil==2.9.0
pytz==2024.1
requests==2.31.0
six==1.16.0
tzdata==2024.1
urllib3==2.2.1
```

### Installing from requirements.txt:

```bash
(venv) $ pip install -r requirements.txt
```

**Use case:** Share your project with others - they can recreate the exact same environment!

---

## 🔍 Checking Virtual Environment Info

### Is a virtual environment active?

```bash
python3 -c "import sys; print(sys.prefix)"
```

**If virtual environment is active:**
```
/Users/yourname/project/venv
```

**If NOT active:**
```
/opt/homebrew/Cellar/python@3.13/3.13.3/Frameworks/Python.framework/Versions/3.13
```

### Which Python is being used?

```bash
which python3
# or on Windows:
where python
```

### What packages are installed?

```bash
pip list
```

---

## 🗑️ Deleting a Virtual Environment

Virtual environments are just folders - delete them like any folder:

```bash
# Make sure it's NOT activated first!
deactivate

# Delete the folder
rm -rf myenv      # Mac/Linux
# or
rmdir /s myenv    # Windows
```

**Important:** Never commit virtual environment folders to Git!

---

## 🎯 Best Practices

### ✅ DO:

1. **Create a venv for EVERY project**
   ```bash
   python3 -m venv venv
   ```

2. **Use common names like `venv`, `env`, or `.venv`**
   - Makes it obvious what it is
   - Easier to remember

3. **Add to `.gitignore`**
   ```
   venv/
   env/
   .venv/
   ```

4. **Use `requirements.txt`**
   ```bash
   pip freeze > requirements.txt
   ```

5. **Activate before working**
   ```bash
   source venv/bin/activate
   ```

### ❌ DON'T:

1. **Don't commit venv folders to Git** - huge and unnecessary
2. **Don't move venv folders** - paths are hardcoded
3. **Don't edit files inside venv/** - let pip handle it
4. **Don't forget to activate** - packages will install globally
5. **Don't use system-wide packages in projects** - use venv

---

## 🧪 Practical Example: Web Scraping Project

Let's create a complete project with a virtual environment:

### Step-by-Step:

```bash
# 1. Create project folder
mkdir web_scraper
cd web_scraper

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate

# 4. Install required packages
pip install requests beautifulsoup4

# 5. Create requirements file
pip freeze > requirements.txt

# 6. Create Python script
cat > scraper.py << 'EOF'
import requests
from bs4 import BeautifulSoup

print("Virtual environment is working!")
print(f"Requests version: {requests.__version__}")
print(f"BeautifulSoup is ready to use!")
EOF

# 7. Run the script
python3 scraper.py

# 8. Deactivate when done
deactivate
```

**Output:**
```
Virtual environment is working!
Requests version: 2.31.0
BeautifulSoup is ready to use!
```

---

## 📂 Project Structure Example

```
my_python_project/
├── venv/                    # Virtual environment (don't commit)
├── src/                     # Your source code
│   ├── __init__.py
│   └── main.py
├── tests/                   # Test files
│   └── test_main.py
├── requirements.txt         # Dependencies (commit this!)
├── .gitignore              # Ignore venv/
└── README.md               # Project documentation
```

**.gitignore example:**
```
# Virtual Environment
venv/
env/
.venv/

# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/

# IDE
.vscode/
.idea/
```

---

## 🔄 Upgrading Packages in Virtual Environment

### Upgrade a specific package:

```bash
(venv) $ pip install --upgrade requests
```

### Upgrade pip itself:

```bash
(venv) $ pip install --upgrade pip
```

### Upgrade all packages (carefully!):

```bash
(venv) $ pip list --outdated
(venv) $ pip install --upgrade package_name
```

---

## 🆚 Virtual Environment vs Global Installation

| Aspect | **Virtual Environment** | **Global Installation** |
|--------|------------------------|------------------------|
| **Location** | Project folder (venv/) | System-wide | 
| **Activation** | Needs activation | Always available |
| **Isolation** | ✅ Isolated per project | ❌ Shared everywhere |
| **Version Conflicts** | ✅ No conflicts | ❌ One version only |
| **Permissions** | ✅ No sudo needed | ❌ May need sudo |
| **Portability** | ✅ Easy with requirements.txt | ❌ Hard to replicate |
| **Best For** | All projects | System tools only |

---

## 🐚 Alternative: virtualenv (Third-party)

Python 3.3+ has built-in `venv`, but there's also `virtualenv`:

### Installation:

```bash
pip install virtualenv
```

### Creating environment:

```bash
virtualenv myenv
```

### Differences:

- **venv:** Built-in, simpler, newer
- **virtualenv:** Third-party, more features, works with Python 2

**Recommendation:** Use `venv` (built-in) for Python 3 projects.

---

## 🎓 Common Command Reference

```bash
# CREATE virtual environment
python3 -m venv venv

# ACTIVATE (Mac/Linux)
source venv/bin/activate

# ACTIVATE (Windows)
venv\Scripts\activate

# CHECK if active
echo $VIRTUAL_ENV                    # Mac/Linux
echo %VIRTUAL_ENV%                   # Windows

# INSTALL package
pip install package_name

# LIST installed packages
pip list

# SAVE dependencies
pip freeze > requirements.txt

# INSTALL from requirements
pip install -r requirements.txt

# DEACTIVATE
deactivate

# DELETE environment
rm -rf venv                          # Mac/Linux
rmdir /s venv                        # Windows
```

---

## 🚨 Troubleshooting

### Problem: "command not found: python3"

**Solution:** Use `python` instead:
```bash
python -m venv venv
```

### Problem: "venv is not activated when I try to activate"

**Mac/Linux Solution:**
```bash
source venv/bin/activate
# NOT: sh venv/bin/activate
```

**Windows Solution:**
```bash
venv\Scripts\activate.bat          # CMD
venv\Scripts\Activate.ps1          # PowerShell
```

### Problem: "PowerShell script execution disabled"

**Windows PowerShell Solution:**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problem: "Packages still installing globally"

**Check if activated:**
```bash
which python3        # Should show venv path
echo $VIRTUAL_ENV    # Should show venv directory
```

If not showing venv path, activate again.

---

## ✅ You've Learned:

- ✅ What virtual environments are and why they're essential
- ✅ How to create a virtual environment with `venv`
- ✅ How to activate/deactivate virtual environments
- ✅ How to install packages in isolated environments
- ✅ How to use `requirements.txt` for dependency management
- ✅ Best practices for project organization
- ✅ Common commands and troubleshooting

---

## 🎯 Practice Exercise

**Create your first virtual environment:**

1. Create a folder called `test_project`
2. Create a virtual environment named `venv`
3. Activate it
4. Install `requests` library
5. Create `requirements.txt`
6. Deactivate
7. Delete the virtual environment
8. Recreate it and install from `requirements.txt`

**Solution:**
```bash
mkdir test_project && cd test_project
python3 -m venv venv
source venv/bin/activate
pip install requests
pip freeze > requirements.txt
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip list
deactivate
```

---

## 🚀 What's Next?

Now that you understand virtual environments, you're ready to:

- **Learn pip in depth** (installing, managing packages)
- **Start coding Python projects** with isolated dependencies
- **Use Git** without worrying about committing huge venv folders
- **Share projects** with confidence using requirements.txt

**Next Topic:** Installing packages with pip and exploring PyPI (Python Package Index)

---

**Happy Coding! 🐍**

*Remember: ALWAYS use virtual environments for your Python projects!*
