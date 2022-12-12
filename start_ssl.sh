
#!/bin/bash


gunicorn --worker-tmp-dir /dev/shm ssl_enforcer:app -c ssl_config.py --reload