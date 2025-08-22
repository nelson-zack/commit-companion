# Commit Companion

![GitHub release (latest by tag)](https://img.shields.io/github/v/release/nelson-zack/commit-companion)
[![PyPI version](https://img.shields.io/pypi/v/commit-companion.svg)](https://pypi.org/project/commit-companion/)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/commit-companion)
[![Downloads](https://static.pepy.tech/badge/commit-companion)](https://pepy.tech/project/commit-companion)

[![License](https://img.shields.io/github/license/nelson-zack/commit-companion)](LICENSE)

**AI-powered Git commit assistant that summarizes staged changes using GPT.**  
Save time, stay in flow, and write better commit messages — automatically.

---

## Features

- Uses GPT to summarize your staged diffs into clear commit messages
- Supports [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- Tone customization (`neutral`, `casual`, `formal`, `funny`, etc.)
- Git hook integration via `prepare-commit-msg`
- Supports environment variables for default `TYPE` and `TONE`
- Optional auto mode to skip confirmation (for non-interactive use)

---

## 📦 Installation

```bash
pip install commit-companion
```

To use the CLI globally from any directory, install with `--user` or inside a virtual environment.

## Quick Start

Or, to install from source:

```bash
git clone https://github.com/nelson-zack/commit-companion.git
cd commit-companion
pip install .
```

### 2. Add your OpenAI API key:

Commit Companion requires access to the OpenAI API. You can provide your key in one of two ways:

#### Option 1: `.env` file (for local use)

```bash
OPENAI_API_KEY=sk-...
```

#### Option 2: Environment variable (for global use)

Add to your shell config (`~/.zshrc`, `~/.bashrc`, etc):

```bash
export OPENAI_API_KEY="sk-..."
```

Then run:

```bash
source ~/.zshrc   # or ~/.bashrc
```

## Requirements

- Python 3.8 or later
- An OpenAI API key (required for GPT functionality)

## Usage

### Help & Options

To see all available commands and flags:

```bash
commit-companion --help
```

### CLI (manual):

```bash
commit-companion suggest
```

### Git Hook (auto):

Install the Git hook with:

```bash
commit-companion install-hook
```

This creates a .git/hooks/prepare-commit-msg script that auto-generates commit messages using GPT.
By default, it uses --tone neutral and --type feat.

#### Once installed, your flow becomes:

```bash
git add <file>      # Stage your changes
git commit          # Commit Companion will auto-suggest the message
git push            # Push to remote
```

#### Customize per commit:

Override tone or type like this:

```bash
TYPE=fix git commit
TONE=funny git commit
TYPE=fix TONE=funny git commit
```

Uninstall the hook:

```bash
commit-companion uninstall-hook
```

## Roadmap Ideas

- Config file support (.commitcompanion.json)
- VS Code extension
- Web version / hosted API
- ✅ PyPI distribution (available via `pip install commit-companion`)

## Why Use This?

Writing commit messages breaks flow. Commit Companion helps you:

- Stay focused on your code
- Standardize commits with no effort
- Impress your teammates with clear, consistent commit messages

## License

MIT License.

## Contributing

Contributions, suggestions, and issue reports are welcome! To get started:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

## Links

- 📦 [PyPI Package](https://pypi.org/project/commit-companion/)
- 🛠 [GitHub Repository](https://github.com/nelson-zack/commit-companion)
- 📝 [Release Notes](https://github.com/nelson-zack/commit-companion/releases)
