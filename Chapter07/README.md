# 一个基于 Rasa 的订票应用[Demo]


## 特性
### 基于 Entity & Role 的实体识别 

通过 Role 区分语义角色，比如`订从上海去北京的票`将会被解析为`订从[上海]{"entity": "city", "role": "departure"}去[北京]{"entity": "city", "role": "destination"}的票`。

上海和北京都是 city 实体，但有了 role 信息的帮助，Rasa拥有足够的信息区别出发地（`"role": "departure"`）和目的地（`"role": "destination"`）。


### 使用 Form 信息 Entity & Role 的正确地提取 slot

可以更改 Form 的配置，让其可以利用 Role 信息对实体做区分，这里提供了代码示例。

```yaml
forms:
  ticket_form:
    city_depart:
      - type: from_entity
        entity: city
        role: departure
      - type: from_entity
        entity: city
        intent: info_city
    city_arrive:
      - type: from_entity
        entity: city
        role: destination
      - type: from_entity
        entity: city
        intent: info_city
    date:
      - type: from_entity
        entity: date
```

### 正确地处理补充词槽的角色归属

由于 city 实体具有多个不同的 role。由于目前 NLU 只考虑当前对话轮，在多轮对话中，有时必须通过上下文才能区分 city 实体的 role。在这一方面 Rasa 的 slot mapping 可以提供帮助。通过 slot mapping，可以获得如下的效果：

示例 #1：补充目的地
```text 
User:
    订明天去北京的车票
Bot:
    从哪里出发呢？
User:
    上海
Bot：
    确定要购买明天从上海出发到北京的车票么？
User:
    是的
Bot:
    好的，正在为您购买车票！
Bot:
    订票成功
```

示例 #2：补充出发地
```text 
User:
    订明天上海出发的车票
Bot:
    到哪里去呢？
User:
    北京
Bot：
    确定要购买明天从上海出发到北京的车票么？
User:
    是的
Bot:
    好的，正在为您购买车票！
Bot:
    订票成功
```

示例 #3：补充出发地和目的地
```text 
User:
    订明天出发的车票
Bot:
    从哪里出发呢？
User:
   上海
Bot:
    到哪里去呢？
User:
    北京
Bot：
    确定要购买明天从上海出发到北京的车票么？
User:
    是的
Bot:
    好的，正在为您购买车票！
Bot:
    订票成功
```

### 根据 Action 执行结果，选择后续对话线路

实际应用中，Action 的执行结果是不确定的，比如定车票：可能成功也可能失败。本项目将通过编写特定的 story 来完成根据 Action 执行结果（api_succeed 是 True 或者 False），动态影响后续对话线路的功能。

在本项目中，为了演示这一功能：对于目的地为北京的订票任务，Action 都将返回成功（api_succeed = True）；目的地为其他城市的订票任务将会返回失败（api_succeed = False）。


示例 #1：订票成功 
```text 
User:
    订明天上海去北京的车票
Bot:
    确定要购买明天从上海出发到北京的车票么？
User:
    是的
Bot:
    好的，正在为您购买车票！
    <!-- 内部状态： api_succeed = True -->
Bot:
    订票成功
```

示例 #2： 订票失败
```text
User:
    订明天北京去上海的车票
Bot:
    确定要购买明天从北京出发到上海的车票么？
User:
    是的
Bot:
    好的，正在为您购买车票！
    <!-- 内部状态： api_succeed = False -->
Bot:
    购票 API 出现异常，购买失败，请稍后重试!
```


## 安装

```bash
pip install -r ./requirements.txt
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

## 训练

```bash
rasa train
```

## 启动

### Step 1: 启动 action server

```bash
rasa run actions
```

### Step 2: 启动 rasa x
我们使用 rasa x 作为客户端

```bash
rasa x
```

启动后会自动打开浏览器窗口

## FAQ
* Q: 在启动训练或者运行 Rasa 服务器时出现了错误：TypeError: stat: path should be string, bytes, os.PathLike or integer, not NoneType，该怎么解决？
  A：这个错误是由于所需的组件用到了外部下载的预训练模型，在训练或者运行时，组件需要联网，如果这时（偶发性地）网络访问失败，就会产生上面的错误，解决方案就是尝试多运行几次就可以解决这个问题。

## 开发指南
见 develop.md
