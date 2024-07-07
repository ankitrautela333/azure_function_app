import logging
import azure.functions as func
import datetime
import os
bp2=func.Blueprint()
@bp2.function_name(name='newfile2')
@bp2.route(route="newfileroute2",auth_level=func.AuthLevel.ANONYMOUS)
def test_function2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.New pipeline.')
    value=os.getenv("random_value")
    return func.HttpResponse(f"Hello nhi ho gya push azure function app mein new, {value} :value {datetime.datetime.now()}",status_code=200)

@bp2.function_name(name='aisekitaise')
@bp2.route(route="aisekitaise",auth_level=func.AuthLevel.ANONYMOUS)
def aisehiaise(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.New pipeline.')
    value=os.getenv("random_value")
    return func.HttpResponse(f"Hello aisekitaise ho gya push azure function app mein new, {value} :value {datetime.datetime.now()}",status_code=200)

@bp2.function_name(name='Time_trigger_one')
@bp2.time_trigger(schedule="0 */3 * * * *",run_on_startup=True)
def time_tig():
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    print('Printed Python timer trigger function ran at %s', utc_timestamp)