from setuptools import setup

setup(
    name='task_manager',
    version='0.1',
    install_requires=[
        line.strip() for line in open('requirements.txt').readlines()
    ],
)
