# KnockIt

Description
------------
Knockit is a simple port knocking client.

Requirements
-------------
* Python 3.x.x

Usage
-------------
```
usage: knockit.py [-h] [-d DELAY] host ports [ports ...]

positional arguments:
  host                  Hostname or IP address of the host.
  ports                 Port(s) to knock on

optional arguments:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        Delay between each knock. Default is 200 ms.
```

Examples
-------------
* Simple port knocking example: 
`python knockit.py 127.0.0.1 23 25 8080`

```
[+] Knocking on port 127.0.0.1:23
[+] Knocking on port 127.0.0.1:25
[+] Knocking on port 127.0.0.1:8080 
```