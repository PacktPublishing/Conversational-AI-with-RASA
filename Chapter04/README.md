## 安装
```bash
bash ./install_dependency.bash
```


## 训练
本项目可以使用 GUI 来训练，但是如果出现错误, 难以调试, 因此目前推荐使用命令行来训练
```bash
rasa train
```


## 启动
### 启动 action server
```bash
SENIVERSE_KEY=xxxx rasa run actions
```

`xxxx` 部分应该替换成从 [心知天气](https://www.seniverse.com/) 申请获得的 API key 。用户可以免费注册，注册后可以在后台找到 `我的API密钥`。

### 启动 rasa x
```bash
rasa x --enable-api --auth-token 12345678
```

启动后会自动打开浏览器窗口


## 使用
### GUI 训练模型 (使用命令行训练后，请忽略本步骤)
在 rasa x 左侧菜单栏，点击 `训练` 按钮，训练模型

### 设定为 production model
在 rasa x 左侧菜单栏，点击 `models` 菜单进入模型管理，鼠标放到模型上，在其右边会出现 `...` 按钮，点击后，将之选择为 `production`。

### 人机对话
在 rasa x 左侧菜单栏，点击 `Talk to your bot` 菜单进入 人机对话界面