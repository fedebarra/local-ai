# Local AI 🚀

This project helps you run several useful tools on your own computer using Docker. These tools work together to help you manage data, use AI models locally, create text-to-speech audio, convert documents, and more.

---

## What is this project? 🤖🛠️

This project sets up a group of services on your computer using Docker. Each service does something helpful:

- **n8n 🤝**: A tool to connect different apps and automate tasks without coding.
- **Baserow 🗂️**: A simple online database where you can store and organize your data.
- **Qdrant 🔍**: A fast system to search and find information based on meaning, useful for AI.
- **Ollama 🧠**: A platform to run large language AI models right on your computer.
- **Kokoro TTS 🗣️**: Turns text into spoken audio (text-to-speech).
- **Gotenberg 📄**: Converts files to PDF format.
- **Pandoc UI 📚**: Converts documents from one format to another with a simple interface.
- **PostgreSQL 🛢️**: A powerful database system that stores all your data safely.

All these services run together and can talk to each other, making it easier to build AI applications and manage your data locally.

---

## What you need before starting 📝

1. **Docker**: Software that lets you run applications inside containers on your computer.
2. **Docker Compose**: A tool to start and manage multiple Docker containers at once.

If you don’t have these installed, here are simple guides:

- [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose is included with Docker Desktop on Windows and Mac. For Linux, follow [this guide](https://docs.docker.com/compose/install/).

---

## Installation 🛠️

### Windows 💻

1. Download and install **Docker Desktop** from [https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/).
2. Install **Git** from [https://git-scm.com/download/win](https://git-scm.com/download/win).
3. Open **PowerShell** or **Command Prompt**.
4. Run the following commands to download and start the project:

   ```
   git clone https://github.com/n8n-io/local-ai.git
   cd local-ai
   docker compose up -d
   ```

### Mac 🍏

1. Download and install **Docker Desktop** from [https://docs.docker.com/docker-for-mac/install/](https://docs.docker.com/docker-for-mac/install/).
2. Install **Git** via Homebrew (`brew install git`) or from [https://git-scm.com/download/mac](https://git-scm.com/download/mac).
3. Open **Terminal**.
4. Run the following commands to download and start the project:

   ```
   git clone https://github.com/n8n-io/local-ai.git
   cd local-ai
   docker compose up -d
   ```

### Server 🖥️ (Linux)

1. Install **Docker** by following the instructions at [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/).
2. Install **Docker Compose** by following [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/).
3. Install **Git** using your package manager, e.g., `sudo apt install git`.
4. Open your terminal.
5. Run the following commands to download and start the project:

   ```
   git clone https://github.com/n8n-io/local-ai.git
   cd local-ai
   docker compose up -d
   ```

---

## How to download this project 🗂️

1. Open a terminal or command prompt on your computer.
2. Type this command to download the project files from GitHub:

   ```
   git clone https://github.com/n8n-io/local-ai.git
   ```

3. Change into the project folder:

   ```
   cd local-ai
   ```

If you don’t have Git installed, you can download the project as a ZIP file from the GitHub page and unzip it.

---

## How to start all services ▶️

1. In the terminal, make sure you are inside the `local-ai` folder.
2. Run this command to start all the services in the background:

   ```
   docker compose up -d
   ```

3. Docker will download all needed images and start the services. This might take some time the first time.

---

## How to open each service in your web browser 🌐

Once all services are running, you can open their web pages by typing these addresses in your browser:

- **n8n 🤝 (Automation tool)**: [http://localhost:5678](http://localhost:5678)
- **Baserow 🗂️ (Database)**: [http://baserow:8080](http://baserow:8080)
- **Qdrant 🔍 (Vector search)**: [http://localhost:6333](http://localhost:6333)
- **Ollama 🧠 (Local AI models)**: No web interface; used by n8n internally.
- **Kokoro TTS 🗣️ (Text-to-Speech)**: [http://localhost:50021](http://localhost:50021)
- **Gotenberg 📄 (PDF converter)**: No web interface; used by other services.
- **Pandoc UI 📚 (Document converter)**: [http://localhost:3001](http://localhost:3001)
- **PostgreSQL 🛢️ (Database)**: No web interface; accessed by other services.

---

## How to stop all services ⏹️

To stop everything, run this command in the project folder:

```
docker compose down
```

This will stop and remove the running containers but keep your data.

---

## Troubleshooting 📝

- **Ports already in use**: If you get an error that a port is busy, another program might be using it. You can:
  - Close the program using that port.
  - Change the port number in the `docker-compose.yml` file before starting.
- **Slow downloads**: The first time you run `docker compose up -d`, Docker downloads large files. This can take a while depending on your internet speed. Please be patient.
- **Docker not found**: Make sure Docker is installed and running before starting.
- **Git not found**: If `git clone` doesn’t work, install Git or download the ZIP from GitHub manually.

---

If you follow these steps, you will have a powerful local setup with AI and productivity tools ready to use!
