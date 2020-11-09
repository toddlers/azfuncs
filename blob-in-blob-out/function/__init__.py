import logging
import azure.functions as func

def main(msg: func.QueueMessage,
inputblob: func.InputStream,
outputblob: func.Out[func.InputStream]) -> None:
    logging.info('Queue item id:%s, body:%s, expiration_time:%s', 
            msg.id, msg.get_body().decode('utf-8'), msg.expiration_time)
    #https://github.com/Azure/azure-functions-python-worker/issues/576
    # logging.info(f'Python Queue trigger function processed : {inputblob.name}') 
    clear_text = inputblob.read()
    logging.info(f'Clear text :{clear_text}')
    outputblob.set(inputblob)

