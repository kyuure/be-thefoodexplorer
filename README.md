# be-thefoodexplorer

![alt text](https://github.com/kyuure/be-thefoodexplorer/blob/main/img/v1.0.png "Server Topology")
Backend source code for TheFoodExplorer

This project is intended for Capstone Project of team Kramcox Bangkit 2021


## Architecture

### Topology
See [here](https://docs.google.com/presentation/d/1f8nl-JyYW6cXSfhCECTw_V_pQeOYsfTQ-flmfxzbivU/edit?usp=sharing "API Architecture")

### File Structure
```
be-thefoodexplorer/
├── Dockerfile
├── requirements.txt
├── app.py
├── scr
│   ├── getfood.py
│   ├── help.py
│   └── searchfood.py
└── .github
    └── workflows
        └── GCP-Deploy.yaml
```


## Run docker image locally
```sh
git clone https://github.com/kyuure/be-thefoodexplorer.git && cd be-thefoodexplorer
docker build -t be-thefoodexplorer .
docker run -p 8080:5000 be-thefoodexplorer
```
