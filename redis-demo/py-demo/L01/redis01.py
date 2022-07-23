import redis   # 导入redis 模块

"""
    使用直连方式链接
"""

ip = "node3"

def demo1():
    r = redis.Redis(host=ip, port=6379, decode_responses=True, password='123456')
    r.set('name', 'runoob')  # 设置 name 对应的值
    print(r['name'])
    print(r.get('name'))  # 取出键 name 对应的值
    print(r['test'])
    print(type(r.get('name')))  # 查看类型

def demo2():
    r = redis.Redis(host=ip, port=6379, db=0, password=123456)
    print(r.keys('*'))
    key_list = r.keys('*')
    # 转换为字符串
    for key in key_list:
        print(key.decode())
    # 查看key类型
    print(r.type('webname'))
    # 返回值: 0 或者 1
    print(r.exists('username'))
    # 删除key
    r.delete('webname')
    if "age" in key_list:
        print("删除失败")
    else:
        print("删除成功")

"""
redis string
"""
def demo3():
    # 连接redis服务器
    r = redis.Redis(host=ip, port=6379, db=0, password= '123456')
     # key为database
    r.set('webname', 'www.biancheng.net')
    print(r.get('webname'))
    # mset参数为字典
    r.mset({'username': 'jacak', 'password': '123'})
    print(r.mget('username', 'password'))
    # 查看value长度
    print(r.strlen('username'))

    # 数值操作
    r.set('age', '15')
    r.incrby('age', 5)
    r.decrby('age', 5)
    r.incr('age')
    r.decr('age')
    r.incrbyfloat('age', 5.2)
    r.incrbyfloat('age', -10.5)
    print(r.get('age'))
     # 删除key
    r.delete('username')


"""
Redis列表
"""

def demo4():
    # 建立redis连接
    r = redis.Redis(host=ip, port=6379, db=0, password="123456", decode_responses=True)
    r.lpush('database', 'sql', 'mysql', 'redis')
    # insert mongodb to mysql before
    r.linsert('database', 'before', 'mysql', 'mongodb')
    print(r.llen('database'))
    print(r.lrange('database', 0, -1))
    print(r.rpop('database'))
    # 通过索引获取数据
    print(r.lindex('database',1))
    # 保留指定区间内元素，返回True
    print(r.ltrim('database', 0, 1))

    while True:
        # 如果列表中为空时,则返回None
        result = r.brpop('database', 1)
        if result:
            print(result)
        else:
            break
    r.delete('database')

"""
redis Redis散列
    # 1、更新一条数据的value，若不存在时，则新建这条数据
    hset(key, field, value)
    # 2、读取数据的指定字段属性，返回值为字符串类型
    hget(key, field)
    # 3、批量更新字段属性,参数mapping为字典类型
    hmset(key, mapping)
    # 4、批量读取数据的字段属性
    hmget(key, fields)
    # 5、获取这条数据的所有属性字段和对应的值，返回值为字典类型
    hgetall(key)
    # 6、获取这条数据的所有属性字段，返回值为列表类型
    hkeys(key)
    # 7、删除这条数据的指定字段
    hdel(key, field)
"""
def demo5():
    r = redis.Redis(host=ip, port=6379, db=0, password="123456")
    # 设置一条数据
    r.hset('user1', 'name', 'www.baidu.com')
    # 更新数据
    r.hset('user1', 'name', 'www.biancheng.net')
    # 获取数据
    print(r.hget('user1', 'name'))
    # 一次性设置多个field和value
    user_dict = {
        'password': '123',
        'gender': 'M',
        'height': '175cm'
    }
    r.hmset('user1', user_dict)
    # 获取所有数据,字典类型
    print(r.hgetall('user1'))
    # 获取所有fields字段和所有values值
    print(r.hkeys('user1'))
    print(r.hvals('user1'))

"""
Redis集合
"""
def demo6():
    r = redis.Redis(host=ip, port= 6379, db=1, password="123456")
    r.sadd("set1", "tom")
    r.sadd("set1", "tom")
    r.sadd("set1", "tom1")
    r.sadd("set1", "tom2")
    # 获取name对应的集合的所有成员
    print(r.smembers('set1'))
    r.sadd("set1", "tony")
    # 获取name对应的集合中的元素个数
    print(r.scard("set1"))
    # 检查value是否是name对应的集合内的元素，返回值为True或False
    print(r.sismember("name", "tony"))
    # 随机删除并返回指定集合的一个元素
    print(r.spop("set1"))
    print(r.smembers('set1'))
    r.srem("set1", "tom")
    r.sadd("set2", "tom1")
    print(r.sinter("set1", "set2"))
    r.sadd("set3", "yuki")
    print(r.sunion("set1", "set2", "set3"))




if __name__ =="__main__":
    demo6()