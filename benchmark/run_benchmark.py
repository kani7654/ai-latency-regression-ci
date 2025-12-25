import time
import json
import numpy as np

with open("baseline/baseline.json") as f:
    baseline = json.load(f)["max_latency"]

start = time.time()

for _ in range(500000):
    np.matmul(
        np.random.rand(16, 16),
        np.random.rand(16, 16)
    )

latency = time.time() - start

print("Measured latency:", latency)
print("Allowed max latency:", baseline)

if latency > baseline:
    raise RuntimeError("❌ Performance regression detected")
else:
    print("✅ Performance within limits")
