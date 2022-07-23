## use docker install redis

### 1、Preface

#### 1.1 config file

接下来就是要将redis 的配置文件进行挂载，以配置文件方式启动redis 容器。（挂载：即将宿主的文件和容器内部目录相关联，相互绑定，在宿主机内修改文件的话也随之修改容器内部文件）

1）、挂载redis的配置文件

2）、挂载redis 的持久化文件（为了数据的持久化）。

配置文件位置

liunx 下redis.conf文件位置： /home/redis/myredis/redis.conf

liunx 下redis的data文件位置 ： /home/redis/myredis/data

```
mkdir -p /home/redis/myredis
```

`-p`是不存在就直接创建/home/redis/myredis 文件夹



redis.conf

```sh
# bind 192.168.1.100 10.0.0.1
# bind 127.0.0.1 ::1
#bind 127.0.0.1

protected-mode no

port 6379

tcp-backlog 511

requirepass 000415

timeout 0

tcp-keepalive 300

daemonize no

supervised no

pidfile /var/run/redis_6379.pid

loglevel notice

logfile ""

databases 30

always-show-logo yes

save 900 1
save 300 10
save 60 10000

stop-writes-on-bgsave-error yes

rdbcompression yes

rdbchecksum yes

dbfilename dump.rdb

dir ./

replica-serve-stale-data yes

replica-read-only yes

repl-diskless-sync no

repl-disable-tcp-nodelay no

replica-priority 100

lazyfree-lazy-eviction no
lazyfree-lazy-expire no
lazyfree-lazy-server-del no
replica-lazy-flush no

appendonly yes

appendfilename "appendonly.aof"

no-appendfsync-on-rewrite no

auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

aof-load-truncated yes

aof-use-rdb-preamble yes

lua-time-limit 5000

slowlog-max-len 128

notify-keyspace-events ""

hash-max-ziplist-entries 512
hash-max-ziplist-value 64

list-max-ziplist-size -2

list-compress-depth 0

set-max-intset-entries 512

zset-max-ziplist-entries 128
zset-max-ziplist-value 64

hll-sparse-max-bytes 3000

stream-node-max-bytes 4096
stream-node-max-entries 100

activerehashing yes

hz 10

dynamic-hz yes

aof-rewrite-incremental-fsync yes

rdb-save-incremental-fsync yes

```

### 2、install command

```sh
docker run --restart=always --log-opt max-size=100m --log-opt max-file=2 -p 6379:6379 --name myredis -v /home/redis/myredis/myredis.conf:/etc/redis/redis.conf -v /home/redis/myredis/data:/data -d redis redis-server /etc/redis/redis.conf  --appendonly yes  --requirepass 123456

```

- –restart=always 总是开机启动
- –log是日志方面的
- -p 6379:6379 将6379端口挂载出去
- –name 给这个容器取一个名字
- -v 数据卷挂载
  - /home/redis/myredis/myredis.conf:/etc/redis/redis.conf 这里是将 liunx 路径下的myredis.conf 和redis下的redis.conf 挂载在一起。
  - /home/redis/myredis/data:/data 这个同上
- -d redis 表示后台启动redis
- redis-server /etc/redis/redis.conf 以配置文件启动redis，加载容器内的conf文件，最终找到的是挂载的目录 /etc/redis/redis.conf 也就是liunx下的/home/redis/myredis/myredis.conf
- –appendonly yes 开启redis 持久化
- –requirepass 123456设置密码 
  - 其中123456是密码

### 3、test redis

进入容器

>  命令：docker exec -it <容器名> /bin/bash

此处跟着的redis-cli是直接将命令输在上面了。

```sh
docker exec -it myredis redis-cli
```

进入之后，我直接输入查看命令：

error是没有权限验证。（因为设置了密码的。）

验证密码：

```sh
auth 密码
```


查看当前redis有没有设置密码：（得验证通过了才能输入的）

```sh
config get requirepass
```







