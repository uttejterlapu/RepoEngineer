# RepoEngineer

🤖 **RepoEngineer** is an AI-powered software engineering agent that analyzes repositories, plans code changes, generates implementations, validates them, and automatically creates GitHub Pull Requests.

## Features

- 🧠 Intelligent task planning
- 📂 Repository analysis
- 🔍 Context-aware code retrieval
- 💻 AI-powered code generation
- 👀 Automated code review
- ✅ Build, lint, and test validation
- 🌿 Git branch management
- 🔀 Automated Pull Request creation
- ⚡ Workflow orchestration with LangGraph

## Architecture

```                    
                    User
                      │
                      ▼
              Planner Agent
                      │
                      ▼
        Repository Analyzer Agent
                      │
                      ▼
         Context Retrieval Agent
                      │
                      ▼
              Coding Agent
                      │
                      ▼
             Reviewer Agent
          ┌──────────┴──────────┐
          │                     │
      Changes needed         Approved
          │                     │
          ▼                     ▼
     Coding Agent        Validation Agent
                                │
                    ┌───────────┴───────────┐
                    │                       │
                 Failed                  Passed
                    │                       │
                    ▼                       ▼
              Debug Agent          Test Generation Agent
                    │                       │
                    ▼                       ▼
              Coding Agent      Documentation Agent
                    │                       │
                    └───────────┬───────────┘
                                ▼
                           Git Agent
                                │
                                ▼
                          Pull Request Agent
                                │
                                ▼
                          GitHub Pull Request```

## Tech Stack

- Python
- LangGraph
- OpenAI / GitHub Models
- Pydantic
- GitPython
- GitHub API

## Status

🚧 Under active development.