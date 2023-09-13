python_requirements(
    name="root",
)

python_requirements(
    name="jupyterreqs",
    source="notebook-requirements.txt"
)

pex_binary(
    name="jupyter",
    dependencies=[":jupyterreqs", "src/python:python"],
    script="jupyter-lab",
    # This is important, otherwise you'll get all kinds of errors.
    execution_mode='venv',
)
