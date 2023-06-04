from extension import LnbitsExtension


extension = LnbitsExtension(
    title="Example extension",
    description="This is an example extension",
    name="example"
)

app = extension.get_app()

from views import *
from views_api import *


if __name__ == "__main__":
    extension.run()
