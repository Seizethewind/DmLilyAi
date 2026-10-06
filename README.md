# LilyAi

LilyAi is a modular AI agent platform built with Python and powered by Groq.

The project is designed around independent intelligence domains that separate memory, context, knowledge retrieval, web retrieval, learning, and tool execution.

LilyAi primarily operates through Discord Direct Messages and includes a web administration interface for testing, monitoring, and development.

---

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                   # add GROQ_API_KEY, DISCORD_TOKEN, ADMIN_TOKEN
python -m LilyAiMain.main                              # bot + API + website on http://localhost:8000
```

Open **http://localhost:8000**: the website is served by the same process as the bot. In **Settings**, enter your `ADMIN_TOKEN` (from `.env`).

No keys yet? Leave them empty: the API and DM Simulator run against an offline provider so you can explore the flow.
Run the tests with `python -m unittest discover -s tests -v`.

**Discord setup:** create an application at discord.com/developers, add a bot, enable **Message Content Intent**, copy the token into `DISCORD_TOKEN`, then DM the bot (no server or slash commands needed).

---

## Vision

LilyAi is designed to be:

- Modular
- Provider agnostic
- Infrastructure agnostic
- Maintainable
- Extensible
- DM-first

The goal is to ensure that LilyAi owns its intelligence while external systems remain replaceable.

---

## Features

**Discord Direct Messages** - DM-first interaction, no slash commands, conversation management, user session management

**Web Search** - internet search, content extraction, source processing

**Memory** - user memory, conversation memory, session memory

**Knowledge Retrieval** - document ingestion, embeddings, vector search, Retrieval-Augmented Generation (RAG)

**Learning** - feedback collection, memory learning, knowledge learning, evaluation workflows

**Tools** - tool execution, utility actions, Discord actions

**Frontend** - chat interface, dashboard, settings, relay, DM simulator

**Modes** - four request modes that decide which tools and docs a turn can use (see below)

**Race Simulator** - Monte Carlo time trials of a user's saved veterans (Simulator Mode)

---

## Modes

Lily starts every session in **Chat Mode**. Typing `mode` shows four buttons, and phrases such as `simulator mode` or
`switch to manage mode` switch directly. The switch is handled in code, never by the model, and the mode is kept in the
user's session (it returns to Chat after 30 idle minutes or a restart).

| Mode | Used for | Tools | Game docs in the prompt |
|---|---|---|---|
| **Chat** (default) | everyday chat, web search | web, utility, reminders, umapyoi | no |
| **Manage** | leaderboard, fan gain and the other uma.moe workflow | uma.moe, trainer link, utility, reminders | no |
| **Analyst** | answers from the data docs | game docs, table/affinity calculators, collection | yes |
| **Simulator** | simulating a veteran on a course | `sim_*` tools, utility | no |

If a message looks like it belongs to another mode, Lily answers it and then offers that mode once per session as a
button. A tool from another mode is refused if the model asks for it. The code is in
`LilyAiMain/MainService/Interaction/Modes`, and each tool's mode comes from its `category`.

**Simulator Mode.** Send screenshots of a veteran's *Umamusume Details* screen (skills tab; two or three if the list
scrolls) and they are read by the vision model and saved **per user in the database**. Then ask, for example,
"simulate #1 on Tokyo 2400 turf" or "would adding Corner Recovery help?". Tools: `sim_list_veterans`, `sim_find_skill`,
`sim_list_courses`, `sim_run`. The simulator models a single runner, so skills that depend on other runners are assumed
to trigger and results are for comparing builds, not predicting a race. It needs `tools/sim_data/skills.json` and
`courses.json` (built by the "Build simulator data" workflow); without them the Simulator tools are simply not offered.
Outside Simulator Mode, screenshots still go to the career review. Not to be confused with the web **DM Simulator**,
which is a chat tester.

---

## Technology Stack

| Layer | Choice |
|-------|--------|
| Language | Python |
| AI Provider | Groq (free-tier models) |
| Platform | Discord |
| Deployment | Docker, Render |

---

## Architecture Philosophy

LilyAi is built using a domain-first architecture. Instead of organizing code by technology, LilyAi organizes code by responsibility.

Benefits: easier maintenance, testing, onboarding and scalability; lower coupling; better long-term stability.

---

## Core Domains

| Domain | Responsible for |
|--------|-----------------|
| LilyAiContext | what LilyAi sees |
| LilyAiMemory | what LilyAi remembers |
| LilyAiTool | what LilyAi can do |
| LilyAiWeb | what LilyAi finds online |
| LilyAiRag | what LilyAi knows |
| LilyAiLearning | how LilyAi improves |

---

## Project Structure

```
LilyAi/
├── LilyAiDocs/
├── LilyAiGroqSupport/
├── LilyAiMain/
├── LilyAiContext/
├── LilyAiMemory/
├── LilyAiTool/
├── LilyAiWeb/
├── LilyAiRag/
├── LilyAiLearning/
├── LilyAiCore/
└── LilyAiFrontend/
```

See `LilyAiDocs/Architecture/` for the detailed scaffold, layers and ownership model.

---

## Interaction Flow

```
Discord DM  (or DM Simulator / Chat via the API)
      │
      ▼
LilyAiMain  ── middleware → session lock → router
      │
      ▼
Interaction Layer  (onboarding, forms, polls, menus, feedback, workflows)
      │
      ▼
Core Domains
      ├── Context   builds the prompt
      ├── Memory    user facts, history, sessions
      ├── Rag       document knowledge
      ├── Web       search + page reading (as tools)
      ├── Tool      registry, validation, execution
      └── Learning  feedback, fact extraction, evaluation
      │
      ▼
LilyAiCore  (Groq provider, database, search, config, logging)
```

---

## Frontend Features

**Relay** - connect to a live Discord bot for monitoring, debugging and testing.

**DM Simulator** - simulate Discord conversations without Discord, for prompt, memory, RAG, tool and workflow testing.

---

## Documentation

**LilyAiDocs** - project-wide documentation: Architecture, Development, Deployment, API, Guides.

**LilyAiGroqSupport** - Groq-specific notes: prompting notes, benchmarks, experiments, provider limitations.

---

## Development Rules

- Python-first
- Domain-first architecture
- No business logic inside infrastructure
- No business logic inside providers
- No slash command dependency
- DM-first design
- Modular development

---

## Future Expansion

Potential future domains: LilyAiVoice, LilyAiVision, LilyAiMobile, LilyAiAnalytics, added without modifying existing domains.

---

## License

MIT License
