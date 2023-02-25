import time


def wait_condition(condition, wait_time=5):
    start_time = time.monotonic()
    while not condition and time.monotonic() - start_time < wait_time:
        time.sleep(0.1)
    return condition
