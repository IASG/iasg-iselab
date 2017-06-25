from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='iselab',
    version='0.1',
    packages=['iselab'],
    url='http://iasg.iac.iastate.edu',
    license='MIT',
    author="Keane O'Kelley",
    author_email='kokelley@iastate.edu',
    description='',
    scripts=['iasg-login'],
    install_requires=required
)
