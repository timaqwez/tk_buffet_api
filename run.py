from __future__ import print_function
import os.path

import uvicorn

from api.database import create_tables
from api.main import app
from api.routes import router


app.include_router(router)

if __name__ == '__main__':
    create_tables()
    uvicorn.run("run:app", host="127.0.0.1", port=os.getenv("PORT", default=8000), log_level="info")






