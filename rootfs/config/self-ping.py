#!/usr/bin/env python3
import os
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests
from time import sleep
if __name__ == "__main__":
    if os.getenv("NO_SLEEP") == "1":
        if "APP_DOMAIN" not in os.environ:
            print("APP_DOMAIN unset, terminating...")
            exit()
        app_domain = os.getenv("APP_DOMAIN")
        while True:
            try:
                requests.get(f"{app_domain}")
            except:
                print("Ping failed, retrying...")
                try:
                    requests.get(f"{app_domain}")
                except:
                    print("Cannot ping app, terminating...")
            sleep(25*60)
