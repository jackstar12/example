# views_api.py is for you API endpoints that could be hit by another service

# add your dependencies here

from main import extension

# add your endpoints here


@extension.api.get("/test/{test_data}")
async def api_example(test_data):
    # Do some python things and return the data
    return test_data
