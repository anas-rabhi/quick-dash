from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name='quick-dash',
    version='0.0.0',
    description='Build quick dash apps',
    author='Anas Rabhi',
    author_email='anas.rabhi.hakim@gmail.com',
    python_requires='>=3.7.0',
    url='https://github.com/anas-rabhi/quick-dash',
    install_requires=required,
    include_package_data=True,
    license='MIT'
)