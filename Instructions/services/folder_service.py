from pathlib import Path


class FolderService:

    def get_tree(self):

        root = Path("../Inbox")

        tree = []

        for path in root.rglob("*"):

            if path.is_dir():

                tree.append(
                    str(
                        path.relative_to(root)
                    )
                )

        return tree