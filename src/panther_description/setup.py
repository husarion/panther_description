from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['packages'] = ['panther_description']
d['package_dir'] = {'': 'scripts'}

setup(**d)