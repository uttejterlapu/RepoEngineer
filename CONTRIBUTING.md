# Contributing to RepoEngineer

First of all, thank you for your interest in contributing to **RepoEngineer**! 🎉

RepoEngineer is an open-source AI Software Engineering platform that uses **LangGraph**, **LLMs**, and a **multi-agent architecture** to analyze repositories, implement code changes, validate them, and automatically create GitHub Pull Requests.

Whether you're fixing bugs, improving documentation, designing new agents, or proposing ideas, your contributions are greatly appreciated.

---

# Ways to Contribute

There are many ways to contribute to RepoEngineer:

- 🐛 Fix bugs
- ✨ Implement new features
- 🤖 Build new AI agents
- 📚 Improve documentation
- 🧪 Add tests
- ⚡ Improve performance
- 🔒 Enhance security
- 🏗️ Improve architecture
- 💡 Suggest ideas through GitHub Discussions or Issues

---

# Development Setup

## 1. Fork the Repository

Click **Fork** on GitHub.

## 2. Clone Your Fork

```bash
git clone https://github.com/<your-username>/RepoEngineer.git
````

```bash
cd RepoEngineer
```

---

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create a `.env` file.

Example:

```env
ENDPOINT=
GITAI_API_KEY=
MODEL_NAME=gpt-4.1
TEMPERATURE=0.2
MAX_OUTPUT_TOKENS=4096
```

---

# Development Workflow

1. Create a new branch

```bash
git checkout -b feature/my-feature
```

2. Make your changes.

3. Test your changes.

4. Commit your work.

```bash
git commit -m "feat: add repository analyzer"
```

5. Push your branch.

```bash
git push origin feature/my-feature
```

6. Open a Pull Request.

---

# Coding Guidelines

Please follow these guidelines:

* Follow **PEP 8**
* Use **type hints**
* Keep functions small and focused
* Prefer composition over large classes
* Write meaningful variable names
* Avoid duplicated code
* Keep business logic inside agents
* Keep LangGraph nodes lightweight

---

# Project Architecture

RepoEngineer follows a modular architecture.

```
User Request
      │
      ▼
Planner Agent
      │
      ▼
Repository Analyzer
      │
      ▼
Context Retriever
      │
      ▼
Coding Agent
      │
      ▼
Reviewer Agent
      │
      ▼
Validation Agent
      │
      ▼
GitHub PR Agent
```

Each agent should have a single responsibility.

---

# Commit Message Convention

Examples:

```text
feat: add repository analyzer

fix: resolve planner parsing issue

docs: update README

refactor: simplify workflow state

test: add planner unit tests
```

---

# Pull Requests

Before submitting a Pull Request, please ensure:

* Your code builds successfully.
* Tests pass.
* Documentation has been updated if needed.
* The PR has a clear description.
* The PR references any related issue.

---

# Reporting Bugs

Please use the **Bug Report** issue template when reporting bugs.

Include:

* Steps to reproduce
* Expected behavior
* Actual behavior
* Environment information
* Logs (if available)

---

# Suggesting Features

Before opening a feature request:

* Search existing issues.
* Check the roadmap.
* Explain the motivation.
* Describe the proposed solution.

---

# Good First Issues

If you're new to the project, look for issues labeled:

* `good first issue`
* `help wanted`
* `documentation`

These are great places to start.

---

# Project Principles

RepoEngineer is built around a few core principles:

* Modular agent design
* Clean architecture
* Deterministic tools before AI reasoning
* Strong typing with Pydantic
* Workflow orchestration with LangGraph
* High-quality, maintainable code
* Developer-friendly APIs

---

# Community

Please be respectful and follow our Code of Conduct.

Constructive discussions, thoughtful feedback, and collaborative problem-solving are always encouraged.

---

# Questions

If you have questions, feel free to:

* Open a GitHub Discussion
* Open an Issue
* Submit a draft Pull Request

We're happy to help new contributors get started.

---

# Thank You ❤️

Every contribution—whether it's a bug fix, a documentation improvement, a new feature, or an architectural suggestion—helps make RepoEngineer better.

Thank you for helping build the future of AI-powered software engineering!
