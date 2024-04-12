import os

from woocommerce import API
from typing import List

from src.schemas.woocommerce_product import Product

wcapi = API(
    url="https://mendiahome.com/",  # Reemplaza con la URL de tu tienda WooCommerce
    consumer_key="ck_874817a051883f90dfa1be4278fea087d331b77a", #os.environ["WOOCOMMERCE_CONSUMER_KEY"],  # Reemplaza con tu Consumer Key
    consumer_secret="cs_f6ceb226f6c59721c3fb7babd8275587fc1a64b0", #os.environ["WOOCOMMERCE_CONSUMER_SECRET"],  # Reemplaza con tu Consumer Secret
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

get_woocommerce_products()