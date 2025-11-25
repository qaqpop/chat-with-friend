# coding = utf-8
"""
@author: lichao
@time:202511/24 18:54
"""

import redis


def redis_conn_pool():
    # pool = redis.ConnectionPool(host='redis-12143.c8.us-east-1-3.ec2.cloud.redislabs.com', port=12143,
    #                             decode_responses=True, password='pkAWNdYWfbLLfNOfxTJinm9SO16eSJFx')
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r

