import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


class LLMService:

    def __init__(self):

        api_key = os.getenv("ANTHROPIC_API_KEY")

        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY nicht gefunden.")

        self.client = Anthropic(api_key=api_key)

        self.model = os.getenv(
            "MODEL",
            "claude-sonnet-5"
        )

    def ask(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = 2000,
    ) -> str:

        try:
            response = self.client.messages.create(

                model=self.model,

                max_tokens=max_tokens,

                system=system_prompt,

                messages=[
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )
            
            for block in response.content:

                if block.type == "text":
                    return block.text


            raise ValueError(
                "Claude hat keinen Textblock zurückgegeben."
            )
            # for block in response.content:
            #     print(type(block))

            # return "".join(
            #     block.text
            #     for block in response.content
            #     if hasattr(block, "text")
            # )

        except Exception as e:

            print(e)

            return "Claude konnte nicht erreicht werden."