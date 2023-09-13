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
    execution_mode='venv'
)
