## installation

Beside rasa, you also need install `pyowm`:

```bash
pip install pyowm
```

## Training Rasa models
```shell
rasa train
```

## Start Rasa action server with OWM key
```shell
OWM_KEY=xxx rasa run actions
```

`xxx` is the API key we can get from https://openweathermap.org/

## Start Rasa server
```bash
rasa run --cors "*"
```

## Start web client
```bash
python -m http.server
```

Try to type some queries like `What's the weather today in Shanghai` and see the response.

Have Fun!


## Credits
* `github-markdown.css` from [github-markdown-css](https://github.com/sindresorhus/github-markdown-css) project
* `showdown.min.js` from [Showdown](https://github.com/showdownjs/showdown) project
* `webchat.js` from [Rasa Webchat](https://github.com/botfront/rasa-webchat) project
