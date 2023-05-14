import multiprocessing
import os

host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "8100")
bind_env = os.getenv("BIND", None)

use_bind = bind_env if bind_env else f"{host}:{port}"

graceful_timeout_str = os.getenv("GRACEFUL_TIMEOUT", "15")
timeout_str = os.getenv("TIMEOUT", "30")
keepalive_str = os.getenv("KEEP_ALIVE", "5")
use_loglevel = os.getenv("LOG_LEVEL", "info")

# Gunicorn config variables
loglevel = use_loglevel
workers = 1
bind = use_bind
worker_tmp_dir = "/dev/shm"
graceful_timeout = int(graceful_timeout_str)
timeout = int(timeout_str)
keepalive = int(keepalive_str)
logconfig = "/src/logging_production.ini"
