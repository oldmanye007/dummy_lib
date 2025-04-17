from setuptools import setup, find_packages

setup(
    name='dummy_lib',
    description= 'A dummy library for testing',
    version= '1.0.1',
    license='GNU General Public License v3.0',
    include_package_data=True,
    url='https://github.com/oldmanye007/dummy_lib',
    author = 'oldmanye007',
    packages=find_packages(),
    install_requires=['h5netcdf',
                      'matplotlib',
                      'numpy',
                      'pandas',
                      'scipy'],
    python_requires='>3.9.*'
    )
