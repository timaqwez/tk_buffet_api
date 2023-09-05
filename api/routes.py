from fastapi import Request, APIRouter
from playhouse.shortcuts import model_to_dict
from starlette.responses import FileResponse

from api.database import database
from api.database.models import Category, Product, ProductCategories

router = APIRouter()


@router.get('/all')
async def get_all_info():
    with database:
        products_names = [model_to_dict(product) for product in Product.select(
            Product.id,
            Product.name,
            Product.price,
            Product.image_name,
            Product.count
        )]
        products_extended = [model_to_dict(product) for product in Product.select()]
        categories = [model_to_dict(category) for category in Category.select()]
        result = {
            'products_names': products_names,
            'products_extended': products_extended,
            'categories': categories,
        }
        return result


@router.get('/products/names')
async def get_names():
    with database:
        result = {'values': [model_to_dict(product) for product in Product.select(
            Product.id,
            Product.name,
            Product.price,
            Product.image_name,
            Product.count
        )]}
        return result


@router.get('/products/all')
async def get_all():
    with database:
        result = {'values': [model_to_dict(product) for product in Product.select()]}
        return result


@router.get('/products/{category_id}')
async def get_products_ids_by_category(category_id: int):
    with database:
        products_ids = ProductCategories.select(ProductCategories.product).where(
            ProductCategories.category == category_id)
        products = [model_to_dict(product)['product'] for product in products_ids]
        return {'values': products}


@router.get('/categories')
async def get_categories():
    with database:
        result = {'values': [model_to_dict(category) for category in Category.select()]}
        return result


@router.get("/images/{image_name}")
async def main(image_name: str):
    return FileResponse(path=f'assets/images/{image_name}')
