
#!/bin/bash


gunicorn --worker-tmp-dir /dev/shm main:app -c gunicorn_config.py
