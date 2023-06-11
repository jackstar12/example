# views_api.py is for you API endpoints that could be hit by another service
import time
from timeit import timeit

from lnbits_lib.db import Database

# add your dependencies here

from main import extension, db

# add your endpoints here


@extension.api.get("/test/{test_data}")
async def api_example(test_data):
    res = await db.fetchall("SELECT * FROM example WHERE wallet = ?", (test_data,))
    return res


    # Do some python things and return the data
    return test_data
