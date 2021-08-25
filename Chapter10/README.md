## install rasa-x
```
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

## installation dependency for action

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

## Start interactive learning
```bash
rasa interactive
```

Try to type some queries like `What's the weather today in Shanghai` and see the response.

Have Fun!