```
# terminal 1
docker run -it --name python-demo python:2-alpine sh

# terminal 2
cd /path/to/this/project
docker cp $(pwd)/occupy-tcp-udp-ports.py python-demo:/

# (switch to) terminal 1
/occupy-tcp-udp-ports.py

# (switch to) terminal 2, run command below, 2000 should be returned.
docker exec -it python-demo netstat -apn | grep python | wc -l
```
