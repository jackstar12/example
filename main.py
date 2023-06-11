import uvicorn
from lnbits_extension import LnbitsExtension
from lnbits_lib.db import Database

extension = LnbitsExtension(
    title="Example extension",
    description="This is an example extension",
    name="example"
)

db = Database("ext_example")

from views import *
from views_api import *

app = extension.get_app()

if __name__ == "__main__":
    extension.run()
