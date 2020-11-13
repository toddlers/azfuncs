import datetime
import logging
import feedparser
import hashlib
import datetime
import json

import azure.functions as func

RSS_FEED_URL = 'https://kubernetes.io/feed.xml'

def get_feed():
    feed = feedparser.parse(RSS_FEED_URL)
    retdocs = []
    # latest 5
    latestentries = feed.get('entries')[:5]
    for entry in latestentries:
        idhash = hashlib.sha1(
            entry.get('link').encode('utf-8')
        ).hexdigest()
        retdoc = {
            "id": idhash,
            "title": entry.get('title'),
            "date": entry.get('updated')
        }
        retdocs.append(retdoc)
    return retdocs

def main(mytimer: func.TimerRequest, outdoc: func.Out[func.Document]):
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc
    ).isoformat()
    if mytimer.past_due:
        logging.info('The timer is past due!')
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    try:
        # get feeds
        outdata = {}
        outdata['items'] = get_feed()
        logging.debug(outdata)
        outdoc.set(func.Document.from_json(json.dumps(outdata)))
    except Exception as e:
        logging.error('Error : ')
        logging.error(e)   
