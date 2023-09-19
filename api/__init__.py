from __future__ import print_function

from api.database import create_tables
from api.main import app
from api.routes import router


def create_app():
    create_tables()
    app.include_router(router)
    return app
