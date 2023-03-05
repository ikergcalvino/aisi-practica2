import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis-server', port=6379)

def get_hit_count():
    retries = 3
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'GEI AISI 2022/2023: counter for Iago Domínguez Cameán and Iker García Calviño ({} times)\n'.format(count)
