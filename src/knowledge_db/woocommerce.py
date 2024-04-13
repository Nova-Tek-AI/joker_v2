import os

from woocommerce import API
from typing import List

from src.schemas.woocommerce_product import Product

wcapi = API(
    url="https://mendiahome.com/",  # Reemplaza con la URL de tu tienda WooCommerce
    consumer_key=os.environ["WOOCOMMERCE_CONSUMER_KEY"],
    consumer_secret=os.environ["WOOCOMMERCE_CONSUMER_SECRET"],
    wp_api=True,
    version="wc/v3",
)


def get_woocommerce_products() -> List[Product]:
    products = wcapi.get("products").json()
    catalogo_info = list()
    for product in products:
        wc_product = Product(
            nombre=product["name"],
            id=product["id"],
            categorias=product["categories"],
            descripcion=product["description"],
            precio=product["price"],
            link=product["permalink"],
            casos_de_uso="",
        )
        catalogo_info.append(wc_product)

    return catalogo_info