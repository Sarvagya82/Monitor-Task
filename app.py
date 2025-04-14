from flask import Flask
from prometheus_client import Counter, Gauge, generate_latest, CollectorRegistry
import time
import random

app = Flask(__name__)
registry = CollectorRegistry(auto_describe=True)

REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests', registry=registry)
MEMORY_USAGE = Gauge('app_memory_usage_bytes', 'Memory usage of the application', registry=registry)

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    MEMORY_USAGE.set(random.randint(1000, 5000))
    time.sleep(random.random() * 0.1)  # Simulate some work
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return generate_latest(registry)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
