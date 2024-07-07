import logging
import azure.functions as func
import datetime
bp=func.Blueprint()
@bp.function_name(name='newfile')
@bp.route(route="newfileroute",auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(f"Hello, {datetime.datetime.now()}",status_code=200)
