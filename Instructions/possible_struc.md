Mögliche Struktur für Agenten und prompts:

knowledge-agent/

main.py

agents/
    planner.py
    router.py
    finance.py
    health.py
    structurer.py

services/
    git_service.py
    markdown_service.py
    slack_service.py
    llm_service.py

models/
    intake.py
    task.py
    result.py

prompts/
    planner.md
    finance.md
    health.md