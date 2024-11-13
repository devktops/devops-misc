from prometheus_client import Counter, Gauge, make_wsgi_app
from prometheus_client import start_http_server
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask
import psutil
import time
import random

# Define batch process success/failure metrics
BATCH_SUCCESS = Counter('batch_success_total', 'Count of successful batch operations')
BATCH_FAILURE = Counter('batch_failure_total', 'Count of failed batch operations')

# Define host metrics
CPU_USAGE = Gauge('host_cpu_usage_percent', 'CPU usage percentage')
MEMORY_USAGE = Gauge('host_memory_usage_percent', 'Memory usage percentage')
DISK_USAGE = Gauge('host_disk_usage_percent', 'Disk usage percentage')

# Flask app to serve as the main application
app = Flask(__name__)

@app.route('/')
def home():
    return "Python Application with Prometheus Metrics"

def batch_process():
    """Simulated batch process that randomly succeeds or fails."""
    if random.choice([True, False]):
        BATCH_SUCCESS.inc()
        print("Batch process succeeded.")
    else:
        BATCH_FAILURE.inc()
        print("Batch process failed.")

def collect_host_metrics():
    """Collects metrics for CPU, memory, and disk usage."""
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.virtual_memory().percent)
    DISK_USAGE.set(psutil.disk_usage('/').percent)
    print(f"Host Metrics - CPU: {CPU_USAGE._value.get()}, Memory: {MEMORY_USAGE._value.get()}, Disk: {DISK_USAGE._value.get()}")

# Combine Flask app with Prometheus WSGI app under the `/metrics` endpoint
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    # Start the batch process and metric collection in the background
    from threading import Thread
    def background_task():
        while True:
            batch_process()
            collect_host_metrics()
            time.sleep(5)

    Thread(target=background_task).start()

    # Run the Flask app with Waitress on port 8000
    from waitress import serve
    serve(app, host='0.0.0.0', port=8000)
