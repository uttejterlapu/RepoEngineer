# 🤖 RepoEngineer

> An open-source AI Software Engineer that analyzes repositories, plans changes, writes code, validates implementations, and creates GitHub Pull Requests using LangGraph and LLMs.

---

## 🚀 Overview

RepoEngineer is an open-source AI Software Engineer built to automate software development workflows.

Instead of relying on a single prompt, RepoEngineer breaks software engineering into specialized AI agents coordinated by **LangGraph**. Each agent has a focused responsibility, making the system modular, maintainable, and extensible.

The long-term vision is to build an autonomous software engineer capable of understanding an existing codebase, implementing requested features, validating changes, and opening production-ready GitHub Pull Requests.

---

## ✨ Features

### Current

- ✅ Planner Agent
- ✅ Structured outputs using Pydantic
- ✅ LangGraph workflow orchestration
- ✅ GitHub Models integration
- ✅ Multi-agent architecture

### Coming Soon

- 🚧 Repository Analyzer
- 🚧 Context Retrieval
- 🚧 Coding Agent
- 🚧 Code Reviewer
- 🚧 Validation Agent
- 🚧 Git Integration
- 🚧 Automated Pull Request Creation
- 🚧 Repository Memory
- 🚧 Multi-LLM Support
- 🚧 MCP Integration

---

# 🏗 Architecture

```text
                   User
                     │
                     ▼
             LangGraph Workflow
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
 Planner      Repository Analyzer   Retriever
     │               │                │
     └───────────────┼────────────────┘
                     ▼
               Coding Agent
                     │
                     ▼
              Review Agent
                     │
                     ▼
            Validation Agent
                     │
                     ▼
          Git & Pull Request Agent
```

---

# 🧠 Agent Workflow

1. Planner Agent
   - Understands the user's request.
   - Creates an implementation plan.

2. Repository Analyzer
   - Understands the repository structure.
   - Detects frameworks, languages, and tooling.

3. Context Retriever
   - Finds only the relevant files and code.

4. Coding Agent
   - Generates code patches.

5. Review Agent
   - Reviews generated code for quality and correctness.

6. Validation Agent
   - Runs builds, tests, linting, and type checks.

7. GitHub PR Agent
   - Commits changes and creates a Pull Request.

---

# 🛠 Tech Stack

- Python
- LangGraph
- Pydantic
- OpenAI SDK
- GitHub Models
- GitPython *(planned)*
- Tree-sitter *(planned)*
- pytest

---

# 📂 Project Structure

```text
RepoEngineer/
│
├── app/
│   ├── agents/
│   ├── graph/
│   ├── llm/
│   ├── models/
│   ├── prompts/
│   ├── detectors/
│   └── tools/
│
├── tests/
├── docs/
├── examples/
│
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── ROADMAP.md
└── LICENSE
```

---

# ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/RepoEngineer.git
```

Move into the project.

```bash
cd RepoEngineer
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
ENDPOINT=
GITAI_API_KEY=
MODEL_NAME=gpt-4.1
TEMPERATURE=0.2
MAX_OUTPUT_TOKENS=4096
```

Run the project.

```bash
python -m app.main
```

---

# 🗺 Roadmap

## Phase 1 — Foundation

- [x] Planner Agent
- [x] LangGraph Integration
- [x] GitHub Models
- [x] Structured Outputs

## Phase 2 — Repository Understanding

- [ ] Repository Analyzer
- [ ] Language Detection
- [ ] Framework Detection
- [ ] Package Manager Detection
- [ ] Repository Tree Generation

## Phase 3 — Context Awareness

- [ ] Context Retrieval
- [ ] Symbol Search
- [ ] Semantic Search
- [ ] Vector Memory

## Phase 4 — Code Generation

- [ ] Coding Agent
- [ ] Patch Generation
- [ ] File Editing

## Phase 5 — Quality Assurance

- [ ] Review Agent
- [ ] Validation Agent
- [ ] Test Generation

## Phase 6 — GitHub Automation

- [ ] Branch Creation
- [ ] Commit Generation
- [ ] Pull Request Creation

---

# 🤝 Contributing

We welcome contributions from developers of all experience levels.

You can contribute by:

- Fixing bugs
- Building new agents
- Improving documentation
- Writing tests
- Enhancing architecture
- Suggesting new ideas

Please read **CONTRIBUTING.md** before opening an Issue or Pull Request.

---

# 💡 Project Vision

RepoEngineer is designed to become a complete AI Software Engineer—not just a code generator.

The goal is to create a system that can:

- Understand large repositories
- Plan implementation strategies
- Retrieve relevant context
- Generate high-quality code
- Review its own work
- Validate changes
- Create production-ready Pull Requests

through a modular, extensible multi-agent architecture.

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support the Project

If you find RepoEngineer useful:

- ⭐ Star the repository
- 🐛 Report bugs
- 💡 Suggest features
- 🤝 Contribute code
- 📢 Share the project with others

Every contribution helps make RepoEngineer a better AI Software Engineering platform.
````
