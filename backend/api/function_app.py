import json
import logging

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.function_name(name="cosmosdb_input_output")
@app.route(route="getcount", auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_input(arg_name="inputDoc", database_name="AzureResume",
                        container_name="Counter", sql_query="SELECT * FROM c", 
                        connection="AzureResumeConnectionString")
@app.cosmos_db_output(arg_name="outputDoc", database_name="AzureResume", 
                         container_name="Counter", connection="AzureResumeConnectionString")
def cosmosdb_input_output(req: func.HttpRequest, inputDoc: func.DocumentList, 
                          outputDoc: func.Out[func.DocumentList]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if inputDoc:
        for document in inputDoc:
            count = document["Count"]
            count_info = {"count": document['Count']}
        
            updated_count = count + 1
            document["Count"] = updated_count
        outputDoc.set(inputDoc)
    
    return func.HttpResponse(json.dumps(count_info), status_code=200,
                             mimetype="application/json")