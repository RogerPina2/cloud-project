from setuptools import setup

setup(
    name='cloud-project',
    version='0.2.0',
    packages=['client', 'deploy'],
    entry_points={
        'console_scripts': [
            'client = client.__main__:main',
            'deploy = deploy.__main__:main',
        ]
    }
)