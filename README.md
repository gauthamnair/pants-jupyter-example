An example of how to run jupyter notebooks that depend on code managed by pants.

To run:
```
$ pants run //:jupyter -- --notebook-dir=notebooks/
```

Should open up [this example notebook](notebooks/Example.ipynb) and you should be able to run/edit, etc. Notice that it uses a module defined in `src/python/my_ml_utils.py` and makes seaborn available for notebooks.

