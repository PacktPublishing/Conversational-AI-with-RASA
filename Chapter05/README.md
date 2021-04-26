# 一个基于 Rasa 的 FAQ 机器人[Demo]

适用于基于 Rasa 的 FAQ （Frequently Asked Questions，常见问题）类型任务的入门实战项目

## 特性
### 支持打招呼和说再见 

这是最基础也是最简单的对话机器人技能。

示例 #1:
```text
User:
    你好 
Bot: 
    你好，我是 Silly，我是一个基于 Rasa 的 FAQ 机器人
```

示例 #2:
```text
User:
    拜拜 
Bot: 
　　再见！
```

### FAQ 问答

示例 #1： 
```text
User:
    一般面试几次
Bot: 
    一般情况下，业务部门和人力资源部会同时或者分别安排一次面试。个别特殊职位需要 2 次及以上的面试。
```

示例 #2：
```text
User:
    怎么查询结果
Bot: 
    我们会通过邮件或电话的形式，通知您面试结果。
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

## 数据源 ##
问答数据来源自：

https://www.dajie.com/corp/2752505/discuss/276604.html
