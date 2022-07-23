import redis

"""
redis 通过连接池使用
"""
def demo():
    # 创建连接池并连接到redis，并设置最大连接数量;
    conn_pool = redis.ConnectionPool(host='node3', port=6379, max_connections=10, password="123456", decode_responses=True)
    # 第一个客户端访问
    re_pool = redis.Redis(connection_pool=conn_pool)
    # 第二个客户端访问
    re_pool2 = redis.Redis(connection_pool=conn_pool)
    print(re_pool.get('name'))

if __name__ == "__main__":
    demo()