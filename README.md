# Commit Companion

**AI-powered Git commit assistant that summarizes staged changes using GPT.**  
Save time, stay in flow, and write better commit messages — automatically.

---

## ✨ Features

- 🧠 Uses GPT to summarize your staged diffs into clear commit messages
- 🛠️ Supports [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- 🎭 Tone customization (`neutral`, `casual`, `formal`, `funny`, etc.)
- 🧩 Git hook integration via `prepare-commit-msg`
- ✅ Optional auto mode to skip confirmation (for non-interactive use)

---

## 🚀 Quick Start

### 1. Clone the repo and install dependencies:

```bash
git clone https://github.com/nelson-zack/commit-companion.git
cd commit-companion
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Add your OpenAI key to .env:
```bash 
OPENAI_API_KEY=sk-...
```

## 🔧 Usage

### CLI (manual mode):
```bash
python main.py --tone casual --type feat
```
Will output something like:
```bash
feat: add basic functionality to README.md
```

### Git Hook (auto mode):
To auto-generate messages on git commit, add this to .git/hooks/prepare-commit-msg:
```bash
#!/bin/bash
python3 /full/path/to/main.py --tone neutral --type feat --auto > .git/COMMIT_EDITMSG
```
Make it executable:
```bash
chmod +x .git/hooks/prepare-commit-msg
```
Now every git commit will pre-fill the message with a GPT-generated summary.

## 🧠 Roadmap Ideas
- Config file support (.commitcompanion.json)
- VS Code extension
- Web version / hosted API
- pip install commit-companion CLI packaging

## 💡 Why Use This?
Writing commit messages breaks flow. Commit Companion helps you:
- Stay focused on your code
- Standardize commits with no effort
- Impress your teammates with clear, consistent commit messages

## 📄 License

MIT License.
