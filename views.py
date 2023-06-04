from fastapi import Depends, Request

from extension import ViewsRouter, LnbitsTemplateResponse
#from lnbits.core.models import User
#from lnbits.decorators import check_user_exists
from main import extension

#from . import example_ext, example_renderer

#templates = Jinja2Templates(directory="templates")


views = ViewsRouter()


@views.get("/")
async def index(user = Depends(extension.check_user_exists)):
    return LnbitsTemplateResponse(template='example/index.html', context={'user': user})

# @example_ext.get("/", response_class=HTMLResponse)
# async def index(
#     request: Request,
#     user: User = Depends(check_user_exists),
# ):
#     return example_renderer().TemplateResponse(
#         "example/index.html", {"request": request, "user": user.dict()}
#     )
