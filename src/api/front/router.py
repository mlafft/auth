from fastapi            import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses  import HTMLResponse


router      = APIRouter()
templates   = Jinja2Templates (directory="templates")


@router.get ('/index.html', response_class=HTMLResponse, summary="главная страница", tags=['Front'])
def index (request: Request):
    
    return templates.TemplateResponse (name="index.html", request=request, context={'text':'TEXT!'})


# @router.get ("/lister", response_class=HTMLResponse)
# def index (request: Request):
#     return templates.TemplateResponse(name="lister.html", request=request, context={'text':'TEXT!'})