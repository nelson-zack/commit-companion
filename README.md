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

### 3. Install CLI tool locally:
```bash
pip install --editable .
```

## 🔧 Usage

### CLI (manual):
```bash
commit-companion suggest --tone casual --type feat
```
Will output something like:
```bash
feat: add basic functionality to README.md
```

### Git Hook (auto):
Install the Git hook with:
```bash
commit-companion install-hook
```
This sets up .git/hooks/prepare-commit-msg to auto-fill your commit message using GPT.

To uninstall:
```bash
rm .git/hooks/prepare-commit-msg
```

## 🧠 Roadmap Ideas
- Config file support (.commitcompanion.json)
- VS Code extension
- Web version / hosted API
- PyPI: pip install commit-companion

## 💡 Why Use This?
Writing commit messages breaks flow. Commit Companion helps you:
- Stay focused on your code
- Standardize commits with no effort
- Impress your teammates with clear, consistent commit messages

## 📄 License

MIT License.
