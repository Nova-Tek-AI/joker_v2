from src.services.llm.tools.say_hi import say_hi_in_italian
from langchain_core.tools import tool
from datetime import datetime

# to do:  tell jokes.
# Situation: The user asks the Virtual Agent to tell a joke and the Virtual Agent should respond back in Spanish
def Jokes_in_spanish(txt: str) -> str:
    """Use this tool when you understand the user is asking for a joke and tell a joke back in spanish"""

    jokes_list = ["¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
                  "¿Cuál es el animal más antiguo? La cebra, porque está en blanco",
                  "¿Qué le dice un gusano a otro gusano? No me mires, soy yo",]
    
    time = datetime.now()
    seconds = time.second
    joke = jokes_list[seconds % len(jokes_list)]
    return joke
# Situation: The user asks the Virtual Agent to tell a joke and the Virtual Agent should respond back in Italian

tools = [say_hi_in_italian]
