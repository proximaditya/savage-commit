<div align="center">
  <h1>🔥 Savage-Commit</h1>
  <p><b>Write conventional commits. Get your ego destroyed.</b></p>
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
</div>

<br/>

> *Writing commit messages is tedious. Getting roasted by an AI is humbling.*

**Savage-Commit** is a lightning-fast CLI tool that analyzes your `git diff` using LLMs. It generates a perfect, conventional commit message for your work, and then brutally roasts your code quality from the perspective of an angry Senior Developer.

![Demo](demo.gif)

---

## ⚡ Features

- **Zero Compute Cost:** Uses BYOK (Bring Your Own Key) architecture.
- **Ultra-Fast:** Powered by Groq's Llama-3 70B for near-instant terminal responses.
- **Privacy First:** Keys are stored locally on your machine, never in the cloud.
- **Beautiful UI:** Uses `rich` for gorgeous terminal outputs.

---

## 🛠️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/proximaditya/savage-commit.git
cd savage-commit

# 2. Install requirements
pip install -r requirements.txt
```

---

## 🚀 Usage

Make some changes to your code, stage them, and let the Senior Dev judge you:

```bash
# Stage your changes
git add .

# Face the music
python main.py
```

---

## 🤝 Contributing (Help Us Build!)

This is an open-source project and we want your pull requests! We are actively looking for contributors to help build these upcoming features:

- [ ] **Multi-Model Support:** Add fallback options for Gemini, OpenAI, and Claude APIs.
- [ ] **Global CLI Setup:** Package the script so users can just run `savage` from anywhere on their OS.
- [ ] **Git Hook Integration:** Make it run automatically on `git commit`.

### How to contribute:

1. **Fork** the Project
2. **Create** your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your Changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. **Push** to the Branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](https://github.com/proximaditya/savage-commit?tab=MIT-1-ov-file) for more information. 

*Disclaimer: Don't blame us if the AI hurts your feelings.*
