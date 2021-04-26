# 一个基于 Rasa 的音乐百科应用[Demo]


## 特性
### 支持丰富的查询方式

#### 查询对象列表并要求给出指定对象的属性

示例 #1： 无条件查询歌曲并要求给出指定歌曲（通过 mention) 的专辑属性
```text
User:
    有什么好听的歌曲？
Bot: 
    找到下列歌曲:
    1: 江南
    2: 舞娘
    3: 晴天
User:
    第一首属于什么专辑？
Bot:
    江南的专辑是第二天堂。
```

示例 #2： 无条件查询歌手并要求给出指定歌手（通过名字) 的生日属性
```text
User:
    列出一些歌手 
Bot: 
    找到下列歌手:
    1: 蔡依林
    2: 林俊杰
    3: 刘若英
    4: 周杰伦
User:
    周杰伦的生日 
Bot:
    周杰伦的生日是 1979/01/18。 
```

#### 查询满足特定属性要求的对象列表


示例 #1： 查询歌曲列表并要求歌曲的歌手属性（也就是演唱者）为周杰伦
```text
User:
    给我列出周杰伦的歌曲 
Bot: 
    找到下列歌曲:
    1: 晴天
```

示例 #2： 查询歌手列表并要求歌手的性别属性为男性
```text
User:
    列一些男性歌手 
Bot: 
    找到下列歌手:
    1: 林俊杰
    2: 周杰伦
```

### 支持 Neo4j 知识库 
默认使用 Rasa 内建的内存知识库，也可以选择 Neo4j 作为知识库。两者在业务层面的效果完全一致。


## 安装

```bash
pip install -r ./requirements.txt
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

## 训练

```bash
rasa train
```

## 使用 Neo4j 数据库 
前置要求：系统需要安装有 docker

### [可选]启动&设置 Neo4j 服务器 

如果想要使用基于 Neo4j 的知识库系统，那么你需要启动 Neo4j 并将数据导入数据库。

```bash
docker run --env=NEO4J_AUTH=none --publish=7474:7474 --publish=7687:7687 neo4j:3.5.20
```

### 将知识库数据写入 

```bash
python ./data_to_neo4j.py
```


## 启动

### Step 1: 启动 action server

#### 方案一：使用内建的内存数据库

```bash
rasa run actions
```

#### 方案二：使用 Neo4j

```bash
USE_NEO4J=1 rasa run actions
```

### Step 2: 启动 rasa x
我们使用 rasa x 作为客户端

```bash
rasa x
```

启动后会自动打开浏览器窗口

## FAQ
* Q: 在启动训练或者运行 Rasa 服务器时出现了错误：TypeError: stat: path should be string, bytes, os.PathLike or integer, not NoneType，该怎么解决？
  - A：这个错误是由于所需的组件用到了外部下载的预训练模型，在训练或者运行时，组件需要联网，如果这时（偶发性地）网络访问失败，就会产生上面的错误，解决方案就是尝试多运行几次就可以解决这个问题。

## 开发指南
见 develop.md
