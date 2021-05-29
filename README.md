# be-thefoodexplorer

![alt text](https://github.com/kyuure/be-thefoodexplorer/blob/main/img/v1.4 "Server Topology")
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
1. Copy Firestore Private Key and API KEY to `~` directory.
2. Clone the repo:
    ```sh
    git clone https://github.com/kyuure/be-thefoodexplorer.git && cd be-thefoodexplorer
    ```
3. Move both files (from step 1) inside current folder.
4. Create and run docker:
    ```sh
    docker build -t thefoodexplorer .
    docker run -p 8080:8080 thefoodexplorer
    ```
5. See the docker to test it by go to https://localhost:8080/


## Collaborator
<table>
  <tr>
<td align="center">
  <img src="https://avatars.githubusercontent.com/kyuure" width="100px;" alt="Salsabila Qothrunnada" style="border-radius:50%"/>
  <br/>
  <sub><b>C0080868</b></sub>
  <br/>
</td>
<td align="center">
  <img src="https://avatars.githubusercontent.com/donitan2018" width="100px;" alt="Salsabila Qothrunnada" style="border-radius:50%"/>
  <br/>
  <sub><b>C0080860</b></sub>
  <br/>
</td>
  </tr>
</table>
