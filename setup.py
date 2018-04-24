from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='iselab',
    version='0.2.1',
    packages=find_packages(),
    url='http://iasg.iac.iastate.edu',
    license='MIT',
    author="Keane O'Kelley",
    author_email='kokelley@iastate.edu',
    description='',
    scripts=['iasg-login', 'iasg-web'],
    data_files=[('/usr/local/bin', ['utils/randssh']),
                ('/etc/systemd/system', ['utils/iselab.service']),
                ],
    include_package_data=True,
    zip_safe=False,
    install_requires=required
)
