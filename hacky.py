import pyshark
import requests
import time
from zapv2 import ZAPv2

# Start ZAP proxy
zap = ZAPv2()

# Set target URL
target_url = "https://dev.neveragain.app/"

# Enable ZAP as a proxy for requests
proxies = {
    "http": "http://localhost:8080",
    "https": "http://localhost:8080"
}

# Make requests to the target URL
response = requests.get(target_url, proxies=proxies)

# Wait for ZAP to finish scanning
time.sleep(5)

# Get ZAP alerts
alerts = zap.core.alerts()

# Print the alerts
for alert in alerts:
    print(alert.get('alert'))

# Stop ZAP proxy
zap.core.shutdown()
