```
# terminal 1
docker run -it --name python-demo python:2-alpine sh

# terminal 2
# cd /path/to/this/project
docker cp $(pwd)/occupy-tcp-udp-ports.py python-demo:/

# (switch to) terminal 1
/occupy-tcp-udp-ports.py

# (switch to) terminal 2, run command below, 2000 should be returned.
docker exec -it python-demo sh -c "netstat -apn | grep python | wc -l"
```


Commands to validate gracefully termination which releases all ports when receive kill command(SIGTERM).
```
./occupy-tcp-udp-ports.py -r 2000 65535 &

# Wait until 'Done' is output.

kill $(ps -ef | grep 'occupy' | grep 'python' | awk '{print $1}')
while true; do
  [[ "$(ps -ef | grep 'occupy' | grep 'python' | wc -l)" == "0" ]] && break
  sleep 0.01
done
netstat -apn | wc -l

# '4' will be output, which is the standard output of "netstat -apn"
```
