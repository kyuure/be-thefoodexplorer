# be-thefoodexplorer

![alt text](https://github.com/kyuure/be-thefoodexplorer/blob/main/img/v1.0.png "Server Topology")
Backend source code for TheFoodExplorer


## Architecture
See ![here](https://docs.google.com/presentation/d/1f8nl-JyYW6cXSfhCECTw_V_pQeOYsfTQ-flmfxzbivU/edit?usp=sharing "API Architecture")


## Run docker image locally
```sh
git clone https://github.com/kyuure/be-thefoodexplorer.git && cd be-thefoodexplorer
docker build -t be-thefoodexplorer .
docker run -p 8080:5000 be-thefoodexplorer
```
