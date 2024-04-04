from langchain_core.tools import tool
from datetime import datetime


@tool()
def say_hi_in_italian(txt: str) -> str:
    """Use this tool when you understand the user is saying hi and say hi back in italian"""

    greetings_type_list = ["ciao", "salve", "buongiorno", "buondi", "buonasera"]
    time_now = datetime.now()
    seconds = time_now.second

    greeting = greetings_type_list[seconds % len(greetings_type_list)]
    return greeting
