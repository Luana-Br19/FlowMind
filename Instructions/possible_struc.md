Mögliche Struktur für Agenten und prompts:

Inbox/
    Workshops/ 

    Finanzen/

    Meetings/
        Daily/
        Sprint Planning/
        Sprint Review/
        Sprint Retro/

    Ideas/
        Project/
        Department/
    
    Geschäftsreise/ #z.B. Aufteilung nach Land

Instructions/

    main.py

    agents/
        planner.py
        router.py
        base_agent.py
        general_agent.py
        finance_agent.py
        workshop_agent.py
        meeting_agent.py
        ideas_agent.py
        geschäftsreise_agent.py

    models/
        intake.py
        task.py
        result.py

    prompts/
        workshop.md
        finance.md
        meeting.md
        ideas.md
        geschäftsreise.md

    services/
        git_service.py
        markdown_service.py
        slack_service.py
        llm_service.py
        
    uploads/ #Orginal PDF Dateien

    json/ #Inhalt (Tags, Input, Quellen) -> später automatisch in Unterordner verschieben?

Rückgabefelder Agent:
folder
filename
title
tags
source
topic
key_points
actions

Meeting-Agent: 
meeting-data