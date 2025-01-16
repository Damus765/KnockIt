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
******************************************************
*                                                    *
*  _  __                     _     _____  _          *
* | |/ /                    | |   |_   _|| |         *
* | ' /  _ __    ___    ___ | | __  | |  | |_        *
* |  <  | '_ \  / _ \  / __|| |/ /  | |  | __|       *
* | . \ | | | || (_) || (__ |   <  _| |_ | |_        *
* |_|\_\|_| |_| \___/  \___||_|\_\|_____| \__|       *
*                                                    *
*                                                    *
* KnockIt v1.0                                       *
* Coded by thebish0p                                 *
* https://github.com/thebish0p/                      *
******************************************************


[+] Knocking on port 127.0.0.1:23
[+] Knocking on port 127.0.0.1:25
[+] Knocking on port 127.0.0.1:8080 
```