import socket
import platform
import os

import logging

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s [%(levelname)s] %(message)s",
  handlers=[
    logging.StreamHandler()
  ]
)


def on_starting(server):
  """
  Do something on server start
  """
  logging.info("Server has started")


def on_reload(server):
  """
   Do something on reload
  """
  logging.info("Server has reloaded")


def post_worker_init(worker):
  """
  Do something on worker initialization
  """
  logging.info("Worker has been initialized. Worker Process id –> {}".format(worker.pid))


def worker_int(worker):
  logging.info('worker_int')


def worker_abort(worker):
  logging.info('worker_abort')


def worker_exit(server, worker):
  logging.info('worker_exit')


def on_exit(server):
  logging.info('on_exit')
