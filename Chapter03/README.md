# 一个基于 Rasa 的报时应用[Demo]

适用于 Rasa 初学者的入门实战项目

## 特性
### 支持打招呼和说再见 

这是最基础也是最简单的对话机器人技能。

示例 #1:
```text
User:
    你好 
Bot: 
　　你好，我是 Silly，我可以帮你查询时间、日期和星期几。你可以对我说「现在几点了？」、「今天几号？」或者「明天星期几？」。
```

示例 #2:
```text
User:
    拜拜 
Bot: 
　　再见！
```

### 查询当前时间 

示例： 
```text
User:
    现在几点了
Bot: 
　　xx:xx:xx // x 代表一位数字
```

### 查询日期 

示例 #1：查询当前日期
```text
User:
　　今天几号
Bot: 
　　xxxx-xx-xx // x 代表一位数字
```

示例 #2：查询未来某天的日期
```text
User:
　　明天几号
Bot: 
　　xxxx-xx-xx // x 代表一位数字
```

示例 #3：查询过去某天的日期
```text
User:
　　昨天几号
Bot: 
　　xxxx-xx-xx // x 代表一位数字
```

由于将所有可能的文字日期（例如：明天 春节 五天前）转换成绝对日期(UNIX 时间戳)是不可能的，因此当超出 bot 的处理范围时，bot 需要友好的提示用户，而不是没有响应或者给出技术出错的细节。

示例 #4：超出能够处理的范围时，会有很友善的提示
```text
User:
　　春节几号
Bot: 
　　系统暂不支持'春节'的日期查询
```

### 查询星期几

示例 #1： 查询当前星期几
```text
User:
　　今天星期几
Bot: 
　　星期Ｘ
```

示例 #2： 查询过去或者未来某天星期几
```text
User:
　　明天星期几
Bot: 
　　星期Ｘ
```

和查询日期一样，查询星期几也有类似的出错处理机制。

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
  - A：这个错误是由于所需的组件用到了外部下载的预训练模型，在训练或者运行时，组件需要联网，如果这时（偶发性地）网络访问失败，就会产生上面的错误，解决方案就是尝试多运行几次就可以解决这个问题。

## 开发指南
见 develop.md
