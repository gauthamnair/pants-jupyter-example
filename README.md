An example of how to run jupyter notebooks that depend on code managed by pants.


## setup as a consumer of the libraries

```
$ pants run //:jupyter -- --notebook-dir=notebooks/
```

Should open up [this example notebook](notebooks/Example.ipynb) and you should be able to run/edit, etc. Notice that it uses a module defined in `src/python/my_ml_utils.py` and makes seaborn available for notebooks.

If you want to pull in new changes to the library side, you will have to shut down your server, pull changes and restart.

## setup as a developer of the libraries

If you are actively developing the library side and are using the notebook for iterative testing, you'll want to set up and run jupyter much as you would [set up an IDE](https://www.pantsbuild.org/docs/setting-up-an-ide):
- export a virtual environment and activate it
- set up `PYTHONPATH`
```
$ pants export --py-resolve-format=mutable_virtualenv --export-resolve=python-default
...
Wrote mutable virtualenv for python-default (using Python 3.11.4) to dist/export/python/virtualenvs/python-default/3.11.4

$ source dist/export/python/virtualenvs/python-default/3.11.4/bin/activate
$ export PYTHONPATH="$(pwd)/src/python"
```

and running the notebook:
```
$ jupyter-lab --notebook-dir=notebooks/
```
Then you can do things like make changes to `my_ml_utils.py` and use `importlib.reload(my_ml_utils)` in the notebook to grab the changes.