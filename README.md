# How-to-use-flask-with-blueprint

*python version: 3.7.2* <br/>

After clone this project, do as following: 

#### First of all, create your virtual environment
    ```python
    python -m venv vapp
    ```
#### Run this project
- Windows: 
    ``` PowerShell
    # PowerShell
    $env:FLASK_APP='run'  # run is the name of run.py that omits it's suffix.
    # and some other steps, like:
    $env:FLASK_ENV='development'
    ```
    ```cmd
    rem cmd
    set FLASK_APP='run'
    set FLASK_ENV='development'
    ```

- Linux or MAC
    ```shell
    $ export FLASK_APP=hello.py
    $ export FLASK_ENV='development'
    ```

- Run ~
    ```python
        flask run --no-reload  #I'd like to explain this option later
        # flask run --host=0.0.0.0  # option host let user can access your service not merely from the server machine.
        # or you can run application in thie way:
        # python -m flask run 
    ```

#### Why not just `flask run`
If just run our application with `flask run`, we will catch such a error:
```python
handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
ValueError: signal only works in main thread
```
[There are](https://stackoverflow.com/questions/53522052/flask-app-valueerror-signal-only-works-in-main-thread) some ways to handle this:<br/>
The problem you are facing has to do with a bug in the Flask-SocketIO package which replaces the `flask run` command. Due to this Flask-SocketIO is always used even if you don’t import it. There are several solutions:

1. Uninstall Flask-SocketIO
2. Do not use `flask run` but run the main file of your program, like `python run.py`
3. Disable debugging
4. Disable auto loading if debugging required `flask run --no-reload` <br/>
***Reference to the Flask-SocketIO bug: [issue 817](https://github.com/miguelgrinberg/Flask-SocketIO/issues/817)***
