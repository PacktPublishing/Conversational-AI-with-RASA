## installation

You need docker to use (optional) custom neo4j knowledge base feature, you can find how to install docker to your system at https://www.docker.com/

Beside rasa, you also need install `neo4j` if you want to use (optional) custom neo4j knowledge base feature:

```bash
pip install neo4j~=4.1
```

## Training Rasa models
```shell
rasa train
```

## Start Rasa action server
### with builtin knowledge base
```shell
rasa run actions
```
### with custom neo4j knowledge base
#### start neo4j server
pull docker image:
```bash
docker pull neo4j:4.1
```

run docker:
```bash
docker run --rm --env=NEO4J_AUTH=none --publish=7474:7474 --publish=7687:7687 neo4j:4.1
```

keep this neo4j running.

#### insert graph to neo4j
```bash
python ./data_to_neo4j.py
```

#### Start Rasa action server with custom neo4j knowledge base
```bash
USE_NEO4J=1 rasa run actions
```

## Start Rasa server and client
```bash
rasa shell
```

Try to type some queries like `List me some songs of Sting` and see the response.

Have Fun!


## Explore Graph
After starting Neo4j, you can use the Neo4j browser to perform visualization and GraphQL debugging by visiting http://localhost:7474 , use `neo4j` as username and password.
