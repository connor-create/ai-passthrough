from setuptools import find_packages, setup

setup(
    name='llm_server',
    packages=find_packages(include=['llm_server']),
    version='0.1.0',
    description='A local server to conglomerate all the LLMs into one pass through',
    author='Connor Jaynes',
    license='MIT',
)