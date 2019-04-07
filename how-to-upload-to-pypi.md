Follow the [official intructions](https://packaging.python.org/tutorials/packaging-projects/).

TROUBLESHOOTING
====================

If you experience 403 errors, try:

    touch ~/.pypirc
    echo "
    [server-login]
    repository: https://pypi.python.org/pypi
    username: <YOUR_PYPI_USERNAME>
    password: <YOUR_PYPI_PASSWORD>
    " > ~/.pypirc
    python3 -m twine upload dist/*
