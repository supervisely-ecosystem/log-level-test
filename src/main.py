import time
import os
import supervisely_lib as sly

if __name__ == "__main__":
    print(f"LOGLEVEL={os.environ.get('LOGLEVEL', 'NOT DEFINED')}")
    print(f"logger.level ={sly.logger.level}")

    time.sleep(99999)
    
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
        sly.logger.info(f"warn {i}")
    sly.logger.critical("crucial")
