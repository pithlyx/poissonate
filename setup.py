
from setuptools import setup, find_packages


setup(
    name='poissonate',
    version='1.0',
    license='MIT',
    author="Cody Roberts",
    author_email='pithlyx@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/pithlyx/poissonate',
    keywords='poisson disc sampling',
    install_requires=[
        'numpy',
        'scipy',
    ],

)
