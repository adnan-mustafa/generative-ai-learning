import truststore
truststore.inject_into_ssl()

import time

from langchain_core.runnables import RunnableLambda

def slow_square(x):
    time.sleep(1)          # one second, standing in for a model call
    return x * x

step = RunnableLambda(slow_square)

start = time.time()
print([step.invoke(n) for n in [1, 2, 3]], round(time.time() - start), "s one by one")

start = time.time()
print(step.batch([1, 2, 3]), round(time.time() - start), "s with batch")

start = time.time()
print(step.batch([1, 2, 3], config={"max_concurrency": 2}), round(time.time() - start), "s with max_concurrency=2")