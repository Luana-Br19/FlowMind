from pathlib import Path
from datetime import datetime


class MarkdownService:

    def __init__(self):
        self.base_path = Path("../Inbox")

    def create_markdown(self, data):

        markdown = f"""
            created:: {datetime.now()}

            title:: {data["title"]}

            tags:: {" ".join("#" + tag for tag in data["tags"])}

            source:: {data["source"]}


            ## Thema

            {data["topic"]}


            ## Kernaussagen

            """

        for point in data["key_points"]:
            markdown += f"- {point}\n"


        markdown += """

## Beispiele / Konzepte

"""

        for example in data["examples"]:
            markdown += f"- {example}\n"


        markdown += """

## Ergebnisse & Learnings

"""

        for learning in data["learnings"]:
            markdown += f"- {learning}\n"


        markdown += """

## Offene Fragen

"""

        for question in data["questions"]:
            markdown += f"- {question}\n"


        markdown += """

## Action Items

"""

        for action in data["actions"]:
            markdown += (
                f"- [ ] {action['task']} "
                f"– Verantwortlich: {action['owner']} "
                f"– Deadline: {action['deadline']}\n"
            )


        return markdown


    def save(self, folder, filename, markdown):
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

        # path = Path(folder)

        # path.mkdir(
        #     parents=True,
        #     exist_ok=True
        # )

        # file = path / filename

        # file.write_text(
        #     markdown,
        #     encoding="utf-8"
        # )

        # return file