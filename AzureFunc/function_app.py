import azure.functions as func
import logging

app = func.FunctionApp()

# Learn more at aka.ms/pythonprogrammingmodel

# Get started by running the following code to create a function using a HTTP trigger.

@app.function_name(name="SuperGPT")
@app.route(route="supergpt")
def main(req: func.HttpRequest) -> func.HttpResponse:
     logging.info('Python HTTP trigger function processed a request.')
     ai_name = ""
     ai_role = ""
     ai_goal = ""
     try:
         req_body = req.get_json()
     except ValueError:
        pass
     else:
        ai_name = req_body.get('ai_name')
        ai_role = req_body.get('ai_role')
        ai_goal = req_body.get('ai_goal')

     if ai_name or ai_role or ai_name:
        return func.HttpResponse(f"Hello, ai_name: {ai_name}. ai_role: {ai_role}, ai_goal: {ai_goal}")
     else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )