from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='iselab',
    version='0.2',
    packages=find_packages(),
    url='http://iasg.iac.iastate.edu',
    license='MIT',
    author="Keane O'Kelley",
    author_email='kokelley@iastate.edu',
    description='',
    scripts=['iasg-login', 'iasg-web'],
    install_requires=required
)
