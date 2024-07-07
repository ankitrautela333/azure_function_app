import azure.functions as func
import datetime
import json
import logging
import csv
import codecs
from additional_functions import bp
from third.third_file import bp2
import os
app = func.FunctionApp()

app.register_blueprint(bp)
app.register_blueprint(bp2)
#changed the slots
#Why no change
@app.function_name(name='Firstfunction')
@app.route(route="newroute",auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    value=os.getenv("random_value")
    return func.HttpResponse(f"Hello,{value}:value {datetime.datetime.now()}",status_code=200)

@app.function_name(name='Bloewdrigger')
@app.blob_trigger(arg_name="myblob", path="newcontainer/People.csv", connection="AzureWebJobsStorage")
def test_func(myblob: func.InputStream):
    logging.info(f"Python {myblob.name}")


@app.function_name(name="Blobread")
@app.blob_trigger(arg_name="readfile", path="newcontainer/People2.csv", connection="AzureWebJobsStorage")
def read_blob(readfile: func.InputStream):
    reader=csv.reader(codecs.iterdecode(readfile,"utf-8"))
    for line in reader:
        print(line)
    logging.info(f"reregre {readfile.name}")


@app.function_name(name='Checkdeploy')
@app.route(route="newdeploy",auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    #value=os.getenv("random_value")
    return func.HttpResponse(f"Hello,function deployed {datetime.datetime.now()}",status_code=200)

