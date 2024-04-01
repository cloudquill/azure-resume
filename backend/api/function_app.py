import json
import logging

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.function_name(name="cosmosdb_input_output")
@app.route(route="getcount", auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_input_v3(arg_name="inputDoc", database_name="AzureResume",
                        collection_name="Counter", sql_query="SELECT * FROM c", 
                        connection_string_setting="AzureResumeConnectionString")
@app.cosmos_db_output_v3(arg_name="outputDoc", database_name="AzureResume", 
                         collection_name="Counter", connection_string_setting="AzureResumeConnectionString")
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