Hi Anna!

So, i made first path of test task :
Steps:
1. Find any open source web application that you like, written in Go, Python or PHP.
2. Implement a `Dockerfile` to dockerize this application (or use existing one).
3. Implement a `docker-compose.yaml` spec to run this application in dockerized environment.
- e2e tests which verify that application is running okay in dockerized environment.

The git adress is https://github.com/maxrodkin/flask-in-docker-compose

If i understood right, it`s not necessary to write own application and Dockerfile. I used this source for python flask application https://hub.docker.com/r/jcdemo/flaskapp/ .
Docker , docker-compose was deployed in AWS EC2 cloud.
For e2e testing , you may use your own url as parameter in e2e.py. The sample is in e2e.sh.

And next task shall prepare tomorrow. Is it acceptable?
