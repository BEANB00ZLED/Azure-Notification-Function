import azure.functions as func
import logging
import json

app = func.FunctionApp()

@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="mqtt-messages",
                               connection="HUB_INSTANCE_CONNECTION_STRING") 
def eventhub_trigger(azeventhub: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                azeventhub.get_body().decode('utf-8'))
    event_data = json.loads(azeventhub.get_body().decode('utf-8'))
    temp = event_data['data']['temperature']
    logging.info(f'Temperature is {temp} degrees F')
    