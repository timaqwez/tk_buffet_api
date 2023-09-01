from peewee import CharField, FloatField, IntegerField, Model, PrimaryKeyField, ForeignKeyField
from api.database.base import database


class BaseModel(Model):
    class Meta:
        database = database


class Product(BaseModel):
    id = PrimaryKeyField()
    name = CharField(max_length=64, null=False, unique=True)
    price = FloatField(null=False)
    weight = IntegerField(null=False)
    description = CharField(max_length=256, null=False)
    composition = CharField(max_length=256, null=False)
    expiration_date = IntegerField(null=False)
    manufacturer = CharField(max_length=64, null=False)
    kcal = FloatField(null=False)
    carb = FloatField(null=False)
    count = IntegerField(null=False)
    image_name = CharField(null=False, unique=True)

    class Meta:
        db_table = 'products'


class Category(BaseModel):
    id = PrimaryKeyField()
    name = CharField(max_length=32, null=False, unique=True)

    class Meta:
        db_table = 'categories'


class ProductCategories(BaseModel):
    id = PrimaryKeyField()
    product = ForeignKeyField(Product)
    category = ForeignKeyField(Category)

    class Meta:
        db_table = 'product_categories'


models = (
    Product,
    Category,
    ProductCategories
)
