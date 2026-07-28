from pathlib import Path
import subprocess


class GitService:

    def __init__(self):

        self.repo = Path("/home/opc/app/FlowMind")


    def push(self, category, title):

        status = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=self.repo,
            capture_output=True,
            text=True
        )

        if status.stdout.strip() == "":
            print("Keine Änderungen.")
            return

        subprocess.run(
            ["git", "add", "."],
            cwd=self.repo,
            check=True
        )

        message = f"Add {category}: {title}"

        subprocess.run(
            [
                "git",
                "commit",
                "-m",
                message
            ],
            cwd=self.repo,
            check=True
        )

        subprocess.run(
            [
                "git",
                "push"
            ],
            cwd=self.repo,
            check=True
        )

        print("Git Push erfolgreich.")