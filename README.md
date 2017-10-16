# netbot

Network monitoring bot.

## Features

* Monitor _ping_ time, _upload_ and _download_ bandwidth.
* Save network metrics to CSV files.
* Save network metrics to JSON files.


## Installation

There is no need for installation. Just run the script without arguments:

```
$ python netbot.py
```

It will automatically create the files `metrics.csv` and `metrics.json` in
the current directory if they do not exist yet. Otherwise, it will just append
the data to them.

## Developing

### Setting virtual environment

> Note: This project is being developed under Python 3.6.0. We also recommend
to use `pyenv` to keep the version fixed.

In order to keep Python's version and related libraries under control, we use
virtual environments as provided by `venv` (builtin module in Python since 3.4).
It is a pretty common pattern in development with Python.

If you don't have a virtual envoriment directory set yet, create one and
set `venv` to use it:

```
$ mkdir venv
$ python -m venv ./venv
```

> Note: Remember to add this new directory to `.gitignore`.

To activate the virtual environment, run:

```
$ source ./venv/bin/activate
```

It should now include a `(venv)` string at the beginning of your prompt. It
makes clear that you are running a virtual environment and so all your Python
commands will be provided by `venv`.

From now on, every Python-related command you use in this project should be
provided by `venv`. For instance, the output for the `which pip3` command should be similar to this:

```
/home/john_doe/netbot/venv/bin/pip3
```

When running a script in the project, call Python explicitly as in `python main.py`.
**Do not** make the script executable and then call it directly. The reason for
this is that calling it explicitly will use the Python version as defined by `venv` as expected.
If you run the script as an executable, it will check for system's Python
(possibly with the wrong version).

To deactivate the session, simply run:

```
$ deactivate
```

To save the current dependencies, run:

```
$ pip freeze > requirements.txt
```

To install the packages needed for development, run:

```
$ pip install -r requirements.txt
```

### Setup.py

In order to use the package for development, you may find useful to install it.

* To install the package for development:

```
$ python setup.py develop
```

* To really install the package:

```
$ python setup.py install
```

## License

This software is released under the MIT license.
