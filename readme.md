## Compose Application

Composeapp is a service & web interface support build & deploy your application use docker-compose.
An example project can be found [here](https://github.com/pmtoan/example-go-service)

### TODO
- User management: CREATE, DELETE, UPDATE, GRANT
- Authenticate user when get app build log

### For Users
#### How it works?
- Firstly, you develop you application with any languages or addition service (database, caching, ...)
- You define a **docker-compose.yml** file describe your application stack
- Use Composeapp to setup and auto build your application

### For Developers
#### Dev environment
- Docker & Docker Compose installed
- Python 3 & NodeJS installed

##### Setup Python Env
Install python virtualenv
```bash
python3 -m pip install virtualenv
```
Create virtualenv for this project
```bash
virtualenv env
```
Install python dependencies
```bash
env/bin/python3 -m pip install -r requirements.txt
```

##### Setup NodeJS Env
Install node modules
```bash
npm install
```
