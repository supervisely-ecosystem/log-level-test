import time
import os
import pprint
import supervisely_lib as sly
from supervisely_lib.sly_logger import LOGGING_LEVELS

if __name__ == "__main__":
    print(f"LOGLEVEL={os.environ.get('LOGLEVEL', 'NOT DEFINED')}")
    print(f"logger.level = {sly.logger.level}")
    pprint.pprint(LOGGING_LEVELS)

    print("trace logs...")
    for i in range(5):
        time.sleep(0.3)
        sly.logger.trace(f"trace {i}")
    print("debug logs...")
    for i in range(5):
        time.sleep(0.3)
        sly.logger.debug(f"debug {i}")
    print("info logs...")
    for i in range(5):
        time.sleep(0.3)
        sly.logger.info(f"info {i}")
    print("warn logs...")
    for i in range(5):
        time.sleep(0.3)
        sly.logger.warn(f"warn {i}")
    sly.logger.critical("crucial")

    #time.sleep(60 * 60) # sleep one hour
