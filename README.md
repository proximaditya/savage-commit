<div align="center">
  <h1>🔥 Savage-Commit</h1>
  <p><b>Write conventional commits. Get your fun message.</b></p>
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
</div>

<br/>

Writing commit messages is tedious. Getting roasted by an AI is humbling. 

**Savage-Commit** is a lightning-fast CLI tool that analyzes your `git diff` using LLMs. It generates a perfect, conventional commit message for your work, and then brutally roasts your code quality from the perspective of an angry Senior Developer.

![Demo](demo.gif)

## ⚡ Features
- **Zero Compute Cost:** Uses BYOK (Bring Your Own Key) architecture.
- **Ultra-Fast:** Powered by Groq's Llama-3 70B for near-instant terminal responses.
- **Privacy First:** Keys are stored locally on your machine, never in the cloud.
- **Beautiful UI:** Uses `rich` for gorgeous terminal outputs.

## 🛠️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/proximaditya/savage-commit.git
cd savage-commit

# 2. Install requirements
pip install -r requirements.txt
