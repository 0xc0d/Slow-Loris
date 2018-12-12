# Slow Loris DDoS Attack

Slowloris is a type of denial of service attack tool invented by Robert "RSnake" Hansen which allows a single machine to take down another machine's web server with minimal bandwidth and side effects on unrelated services and ports.

### Example: 
Using python version 3
```
python slowloris.py www.example.com 80 100 10
# here 80 is the port number
# 100 is total number of socket to create
# 10 is the timer period to check for open socket and create any
```
