### About

This is a web application, providing an interface for getting movie
recommendations for the users.

### Build and run
To build and run application do the following:
1) Clone the project
2) cd to the project directory

3) Build new docker image
```commandline
docker build --no-cache -t movie_rec --target application .
```

4) Run the container
```commandline
docker run -p 5001:5000 movie_rec
```
If the port 5001 on your machine is occupied, change it to whatever you like

5) In your browser navigate to 
**127.0.0.1:5001** or **localhost:5001**, specifying the port from previous point 

6) Use the web interface to get user recommendations 

### Run tests

To run the tests you have two options:
1) cd to the project directory, execute
```commandline
docker build --no-cache --rm -t movie_rec_test --target test .
```
This will create a test container, and run all tests. 
If an error occurs, you will be notified. If the build is successful, 
then all tests passed, container will automatically exit and get deleted. 

2) 
   1) Create a container as specified in **Build and run** point 3
   2) Run container in a detached mode  
   ```commandline
   docker run -p 5001:5000 -d movie_rec
   ```
   3) Enter container interactive shell
   ```commandline
   docker exec -it <container_id> bash
   ```
   4) From the shell run the following
   ```commandline
   python -m unittest tests/run_tests.py
   ```
