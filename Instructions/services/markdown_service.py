from pathlib import Path
from datetime import datetime


class MarkdownService:

    def __init__(self):
        self.base_path = Path("../Inbox")

#     def create_markdown(self, data):

#         markdown = f"""
#             created:: {datetime.now()}

#             title:: {data["title"]}

#             tags:: {" ".join("#" + tag for tag in data["tags"])}

#             source:: {data["source"]}


#             ## Thema

#             {data["topic"]}


#             ## Kernaussagen

#             """

#         for point in data["key_points"]:
#             markdown += f"- {point}\n"


#         markdown += """

# ## Beispiele / Konzepte

# """

#         for example in data["examples"]:
#             markdown += f"- {example}\n"


#         markdown += """

# ## Ergebnisse & Learnings

# """

#         for learning in data["learnings"]:
#             markdown += f"- {learning}\n"


#         markdown += """

# ## Offene Fragen

# """

#         for question in data["questions"]:
#             markdown += f"- {question}\n"


#         markdown += """

# ## Action Items

# """

#         for action in data["actions"]:
#             markdown += (
#                 f"- [ ] {action['task']} "
#                 f"– Verantwortlich: {action['owner']} "
#                 f"– Deadline: {action['deadline']}\n"
#             )


#         return markdown


    # def save(self, folder, filename, markdown):
    #     full_path = self.base_path / folder / filename

    #     full_path.parent.mkdir(
    #         parents=True,
    #         exist_ok=True
    #     )

    #     full_path.write_text(
    #         markdown,
    #         encoding="utf-8"
    #     )

    #     return full_path


    def save(self, data, intake):

        markdown = self.create_markdown(data, intake)

        folder = data["folder"]
        filename = data["filename"]

        full_path = self.base_path / folder / filename

        full_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        full_path.write_text(
            markdown,
            encoding="utf-8"
        )

        return full_path


    ####################################################
    # Hauptfunktion
    ####################################################

    def create_markdown(self, data, intake):

        #markdown = ""

        # markdown += f"""created:: {datetime.now().strftime('%d.%m.%Y %H:%M')}
        # title:: {data.get("title","")}
        # tags:: {" ".join("#"+t for t in data.get("tags", []))}
        # source:: {data.get("source","")}
        # folder:: {data.get("folder","")}
        
        markdown = f"""
        
        created:: {datetime.now().strftime('%d.%m.%Y %H:%M')}

        title:: {data.get("title","")}

tags:: {" ".join("#"+t for t in data.get("tags", []))}

        source:: {data.get("source","")}

        folder:: {data.get("folder","")}

        agent:: {intake.category}

        id:: {intake.id}

links:: [[{"[[".join(t + "]], " for t in data.get("tags", []))}


#  {data.get("title","")}

## Thema

{data.get("topic","")}

"""

        if data.get("summary"):
            markdown += f"""## Zusammenfassung

            {data["summary"]}

"""

        self._write_list(
            markdown_ref := [markdown],
            "Kernaussagen",
            data.get("key_points")
        )

        self._write_actions(
            markdown_ref,
            data.get("actions")
        )

        markdown = markdown_ref[0]

        category = data.get("category")

        specific = data.get("specific_data", {})

        if category == "Workshop":
            markdown += self._workshop(specific)

        elif category == "Meeting":
            markdown += self._meeting(
                specific,
                data.get("meeting_type")
            )

        elif category == "Ideas":
            markdown += self._ideas(specific)

        elif category == "Geschäftsreise":
            markdown += self._travel(specific)

        elif category == "Finanzen":
            markdown += self._finance(specific)

        return markdown


    ####################################################
    # Hilfsmethoden
    ####################################################

    def _write_list(self, md, title, values):

        if not values:
            return

        md[0] += f"\n## {title}\n\n"

        for value in values:
            md[0] += f"- {value}\n"


    def _write_actions(self, md, actions):

        if not actions:
            return

        md[0] += "\n## Action Items\n\n"

        for action in actions:

            if isinstance(action, str):

                md[0] += f"- [ ] {action}\n"

            else:

                md[0] += (
                    f"- [ ] {action.get('task','')}"
                    f" – Verantwortlich: {action.get('owner','')}"
                    f" – Deadline: {action.get('deadline','')}\n"
                )


    ####################################################
    # Workshop
    ####################################################

    def _workshop(self, data):

        md = ""

        self._append_list(md_ref := [md], "Beispiele / Konzepte", data.get("examples"))

        self._append_list(md_ref, "Ergebnisse & Learnings", data.get("learnings"))

        self._append_list(md_ref, "Offene Fragen", data.get("questions"))

        return md_ref[0]


    ####################################################
    # Meeting
    ####################################################

    def _meeting(self, data, meeting_type):

        md = f"\n# {meeting_type}\n\n"

        for key, value in data.items():

            md += f"## {key.replace('_',' ').title()}\n"

            if isinstance(value, list):

                for item in value:
                    md += f"- {item}\n"

            else:
                md += f"{value}\n"

            md += "\n"

        return md


    ####################################################
    # Ideas
    ####################################################

    def _ideas(self, data):

        md = ""

        mapping = {
            "problem":"Problem",
            "solution":"Lösung",
            "benefit":"Nutzen",
            "effort":"Aufwand"
        }

        for key, title in mapping.items():

            if data.get(key):

                md += f"\n## {title}\n\n"

                md += f"{data[key]}\n"

        self._append_list(
            md_ref := [md],
            "Risiken",
            data.get("risks")
        )

        self._append_list(
            md_ref,
            "Offene Fragen",
            data.get("questions")
        )

        return md_ref[0]


    ####################################################
    # Geschäftsreise
    ####################################################

    def _travel(self, data):

        md = ""

        for key, value in data.items():

            md += f"\n## {key.replace('_',' ').title()}\n\n"

            if isinstance(value, list):

                for item in value:
                    md += f"- {item}\n"

            else:

                md += f"{value}\n"

        return md


    ####################################################
    # Finanzen
    ####################################################

    def _finance(self, data):

        md = "\n## Rechnungsdetails\n\n"

        for key, value in data.items():

            md += f"- **{key.replace('_',' ').title()}**: {value}\n"

        return md


    ####################################################
    # interne Hilfsmethode
    ####################################################

    def _append_list(self, md, title, values):

        if not values:
            return

        md[0] += f"\n## {title}\n\n"

        for value in values:
            md[0] += f"- {value}\n"