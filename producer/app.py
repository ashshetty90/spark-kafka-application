from event_broadcaster import Broadcaster
import logging,time
import json

dispatcher = Broadcaster()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
if len(logger.handlers) == 0:
    logger.addHandler(logging.StreamHandler())



def post_event():
    """
    mocking the behaviour of a json stream by pushing events into the kafka producer stream
    """
    with open('mock_data.json') as data_file:
        data = json.load(data_file)
        for request_json in data:
            logger.debug("request had the following data: {0}".format(request_json))
            dispatcher.push(request_json)
            time.sleep(10)


if __name__ == '__main__':
    post_event()
