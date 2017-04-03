import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup
sys.path.append("..")
import optimize_upip

setup(name='micropython-uterkin',
    version='0.0.1',
    description='MicroPython module for data acquisition and telemetry',
    url='https://github.com/daq-tools/terkin',
    author='Terkin Developers',
    author_email='developers@terkin.org',
    maintainer='Terkin Developers',
    maintainer_email='developers@terkin.org',
    license='Python',
    cmdclass={'optimize_upip': optimize_upip.OptimizeUpip},
    packages=['uterkin'],
    install_requires=[
        'micropython-copy', 'micropython-json',
        'micropython-http.client', 'micropython-io', 'micropython-time',
        'micropython-umqtt.robust', 'micropython-umqtt.simple'
    ]
)
