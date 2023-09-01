from api.database.base import database
from api.database.models import models, Product


def create_tables():
    database.create_tables(models=models)
    with database:
        try:
            Product.get_or_create(
                name='Батончик Snickers',
                price=2.29,
                description='Сладкий и сбалансированный вкус. '
                            'Хрустящий арахис обёрнут карамелью, '
                            'покрытый мягкой нугой и шоколадом. '
                            'Удовольствие в каждом укусе.',
                weight=55,
                composition='нуга, карамель',
                expiration_date=8760,
                manufacturer='ООО Марс Компани',
                kcal=111,
                carb=12,
                count=13,
                image_name='snickers.png',
            )
            Product.get_or_create(
                name='Батончик Twix',
                price=2.39,
                description='Нежный вкус сливочной карамели, '
                            'покрытой хрустящим печеньем и '
                            'густым шоколадом — идеальное '
                            'сочетание текстур и вкусов.',
                weight=55,
                composition='шоколад, печенье, карамель',
                expiration_date=8760,
                manufacturer='ООО Марс Компани',
                kcal=127,
                carb=13,
                count=0,
                image_name='twix.png',
            )
            Product.get_or_create(
                name='Батончик Марс',
                price=1.99,
                description='Изысканный вкус: нежная нуга, сладкая '
                            'карамель, арахис и шоколад в одном '
                            'батончике. Разнообразие вкусов, '
                            'создающее неповторимую гармонию.',
                weight=55,
                composition='нуга, шоколад',
                expiration_date=8760,
                manufacturer='ООО Марс Компани',
                kcal=144,
                carb=14,
                count=33,
                image_name='mars.png',
            )
        except:
            pass
