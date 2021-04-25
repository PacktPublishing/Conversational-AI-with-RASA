# 一个基于 Rasa 的天气查询机器人

一个使用 Rasa 技术栈 （Rasa NLU, Rasa Core, Rasa Core SDK）构建的简单的中文天气情况问询机器人(chatbot), 附带有基于 Web 的用户界面（UI）

## 功能
这个机器人可以根据你提供的城市（北京、上海等）和日期（明天、后天等），查询出相应的天气预报。

## 功能截图
<img src="images/weather_bot_query_interface.png" width="50%">

## 特性
使用 Frame-based 对话管理方案，如果上述两个 Slot (既城市和天气)，有任意一个用户未提供，对话管理系统会负责让你澄清相关 Slot 的值。

## 能力范围
* 受限于天气数据提供方的能力，这个机器人只能查询 **中国大陆地区市级城市** 三天以内 **（今天，明天，后天）** 的气象数据，**不能查询过去**（昨天，前天）等历史数据。
* 受限于开发时间，这个机器人 **不提供** 诸如 **这个星期五、下个星期一** 这种需要计算才能得到日期给定方式。也 **不能提供** 诸如 **绝对日期：三月一号、六一儿童节日** 这种日期的查询能力。
* 因为使用的是免费的天气查询接口，所以 **会有配额限制**，可能会因为 **超出调用次数** ，而在一个小时内不能用。同时网络查询接口可能存在不稳定因素，导致 **没有结果返回或者出现异常**，**尝试多次重新发送请求可解决问题**。

## 动画演示
<img src="images/WeatherBot_demo.webp" width="50%">

## 在线演示
[Demo for 天气预报查询机器人](http://weather_bot.xiaoquankong.ai/)

## 环境要求 ##
Mac OS X or Linux

Support Windows but without testing.

## 安装

### 安装依赖 ###
安装 python 等各种软件包依赖

```bash
pip install -r ./requirements.txt
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
pip install git+https://github.com/mit-nlp/MITIE.git
```

### 安装模型文件 ###
下载已经预先训练好的 MITIE 的模型文件（地址：https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/releases/download/0.1/total_word_feature_extractor.dat.tar.gz）

解压缩，将 total_word_feature_extractor.dat 文件拷贝至 bin_data 目录。

## 训练

```bash
rasa train
```

## 使用流程

### Step 1: 启动 action server
```bash
SENIVERSE_KEY=xxxx rasa run actions
```

`xxxx` 部分应该替换成从 [心知天气](https://www.seniverse.com/) 申请获得的 API key 。用户可以免费注册，注册后可以在后台找到 `我的API密钥`。

### Step 2: 启动rasa server ###

```bash
rasa run --cors "*" --credentials ./credentials.yml
```

### Step 3: 启动 Web client ###
```bash
python -m http.server
```

### Step 4: 访问 Web client ###
访问 http://localhost:8000

## FAQ
* 如果在使用机器人中遇到解析失败或者 SSL 错误或者超时错误，请重试几次，数据提供商 `心知天气` 的 API 很不稳定
