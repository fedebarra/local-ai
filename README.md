# Local AI 🚀

This project lets you run powerful AI tools **directly on your computer** — with **full privacy** and **no cloud access required**. Everything runs using **Docker**, and services talk to each other so you can build AI workflows, run local language models, use text-to-speech, speech-to-text, convert files, and more.

---

## What is this project? 🤖🛠️

You get a complete local AI platform:

| Service | Purpose | URL |
|--------|--------|------|
**n8n** 🤝 | Automate tasks, build AI workflows | http://localhost:5678 |
**Qdrant** 🔍 | Vector search for RAG and memory | http://localhost:6333/dashboard |
**Ollama** 🧠 | Run open-source AI models locally (Gemma, Llama, etc.) | *CLI & API only* |
**Kokoro TTS** 🗣️ | Text → Speech | http://localhost:8880/web (/docs for info) |
**Whisper** 🎤 | Speech → Text | http://localhost:8020 (/docs for info)|
**Gotenberg** 📄 | Convert files → PDF | *API service only* |
**MinIO** 📦 | Object storage (S3‑compatible) | http://localhost:9001 |
**PostgreSQL** 🛢️ | Database for n8n | *Internal service* |

All data stays **local and private** ✅

---

## Requirements ✅

Install these first:

### 🐳 Docker Desktop
Runs all services in containers  
https://www.docker.com/products/docker-desktop/

> Windows: enable **WSL2** during install and pick Ubuntu.

### 🧠 Ollama
Runs AI models locally  
https://ollama.com/download

After install, pull a starter model:

```bash
ollama pull gemma3:1b
```

> Smaller models = faster and work on more machines.

### 📝 Visual Studio Code
To open and edit this project  
https://code.visualstudio.com/

---

## Download the project

### Git method (recommended)

```bash
git clone https://github.com/fedebarra/local-ai.git
cd local-ai
```

### ZIP method
- Go to https://github.com/fedebarra/local-ai
- Click **Code → Download ZIP**
- Unzip and open in VS Code

> Windows users: Better performance if stored in WSL:  
`\\wsl$\Ubuntu\home\<you>\local-ai`

---

## ⚙️ Environment Variables (.env)

This folder already includes a `.env` file.

✅ Default values included  
❗ **You MUST open it and change the credentials before running**

Open it in VS Code and edit:

```env
# --- Postgres Credentials ---
POSTGRES_USER=root             # Change to your username
POSTGRES_PASSWORD=password     # Change to a strong password
POSTGRES_DB=n8n                # Leave as is

# --- Cloudflare Tunnel (optional for remote access) ---
TUNNEL_TOKEN= [paste token here]

# --- OpenAI / Ollama ---
OPENAI_API_KEY= [optional, only if using cloud models]
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-4o-mini
MODEL_EMBEDDING_NAME=text-embedding-3-small

# Ollama (local models)
OLLAMA_BASE_URL=http://host.docker.internal:11434
OLLAMA_HOST=host.docker.internal/11434
MODEL_OLLAMA_NAME=gemma3:1b
MODEL_OLLAMA_EMBEDDING_NAME=embeddinggemma:latest

# --- n8n ---
N8N_ENCRYPTION_KEY=your-very-strong-key
N8N_USER_MANAGEMENT_JWT_SECRET=another-strong-secret
N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
WEBHOOK_URL=http://localhost:5678
```

### ✅ Required changes

| Variable | Action |
|---|---|
`POSTGRES_PASSWORD` | Change to your password |
`N8N_ENCRYPTION_KEY` | Replace with long random string |
`N8N_USER_MANAGEMENT_JWT_SECRET` | Replace with long random string |

---

## Start everything ▶️

Open Terminal / PowerShell in project folder:

### CPU mode (recommended for beginners)

```bash
docker compose --profile cpu up -d
```

### GPU mode (only if you have NVIDIA / Apple GPU support)

```bash
docker compose --profile gpu-nvidia up -d
```

---

## Access your tools 🌐

| Service | URL |
|---|---|
n8n | http://localhost:5678 |
Qdrant Dashboard | http://localhost:6333/dashboard |
Pandoc UI | http://localhost:8081 |
MinIO Console | http://localhost:9001 |
Kokoro TTS | http://localhost:8880/web |
Whisper API docs | http://localhost:8020 |

> First launch may take 20–60 seconds — refresh if needed.

---

## Stop the system ⏹️

```bash
docker compose down
```

Keep your data ✅

To erase everything ⚠️

```bash
docker compose down -v
```

---

## Troubleshooting 🧯

| Problem | Fix |
|---|---|
Docker not running | Open Docker Desktop |
Ollama not found | Restart terminal & reinstall |
Ports busy | Stop apps or edit ports in compose |
Windows errors | Move folder to WSL home directory |
Slow models | Use `gemma3:1b` |

---

## You're ready! 🎉

You now run:

- Offline AI chat  
- Workflow automation  
- Local speech AI  
- Private vector search  
- Local storage  
- Document pipelines  

Fully **local, private, and extensible**.


