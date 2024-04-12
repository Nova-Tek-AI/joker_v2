from langchain_core.tools import tool

from src.knowledge_db.woocommerce import get_woocommerce_products


@tool()
def ecommerce_services(txt: str) -> str:
    # this is for the AI Agent to understand the it needs to use this tool under a certain situation
    """
    Utilice esta herramienta cuando comprenda que el usuario está solicitando una recomendación.
    Si hay muchos productos que cumplen con la descripción que brinda el cliente,
    escoge las tres más baratas.

    Ejemplo 1:
    user: "Me gustaría un mueble para mi sala, que podrías recomendarme?"
    you: " ¡Hola! Para tu sala tenemos varias opciones, te muestro 3 de ellas.


    Ejemplo 2:
    user: "Tengo una cita con mi novio, iremos a un restaurante elegente"
    you: " ¡Hola! Una cita es la oportunidad fantastica para sorprender a tu novio. Tenemos justo las prendas y accesorios que necesitas: \n
        1. Sofá Americano. \n
            - 1,90cm de largo. \n
            - 85cm de profundidad. \n
            - 65cm de altura al brazo. \n

            Cuesta desde S/1,900.00. Puedes encontrarlo aquí: https://mendiahome.com/producto/sofa-americano/ \n
        2. Sofá Mila. \n
            - 2,10cm de largo. \n
            - 90cm de profundidad. \n
            - 76cm de altura. \n
            
            Cuesta S/ 1900.00 Puedes encontrarla aquí: https://mendiahome.com/producto/sofa-mila/ \n
        
        ¡gracias por escogernos!
    """

    return get_woocommerce_products()
