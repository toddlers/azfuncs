import logging

import azure.functions as func


def main(documents: func.DocumentList) -> str:
    if documents:
        for document in documents:
            logging.debug("====================================")
            logging.info('Document id: %s', document['id'])
            logging.debug("====================================")

