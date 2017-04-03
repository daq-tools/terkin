###################
micropython-uterkin
###################


*******
Hacking
*******
This is about running the examples inside the working tree, i.e. development mode.

Synopsis::

    # Go to directory
    cd terkin/src/micropython

    # Announce path to micropython binary
    export PATH=$PATH:~/dev/foss/fetched/micropython/unix

    # Run example
    micropython -c 'import sys; sys.path.insert(0, ".")' examples/node_http_json_wan.py



*************
Build package
*************
::

    python3 setup.py sdist

