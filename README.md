# simple-reverse-shell

A reverse shell is a shell session established on a connection that is initiated from a remote machine, not from the local host.

## Installation

Clone the project

```bash
  git clone https://github.com/detth/simple-reverse-shell.git
```

Go to the project directory

```bash
  cd simple-reverse-shell
```



## Usage/Examples

Run shell TCP server(attacker)

#### Linux:
```bash
  python3 shell_server.py
```

#### Windows:
```bash
  py shell_server.py
```

Run client(victim)

#### Linux:
```bash
  python3 shell_client.py
```

#### Windows:
```bash
  py shell_client.py
```
When client is running, you will be auto connected to server.  
If client is connected, you can execute some commands in terminal, like as: ifconfig, ipconfig, notepad.exe etc.

## License

[MIT](https://choosealicense.com/licenses/mit/)
