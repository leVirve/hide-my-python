from setuptools import setup

setup(
  name='hidemypython',
  version='0.1.0',
  description='A parser for the free proxy list on HideMyAss!',
  url='http://github.coom/leVirve/hide_my_python',
  maintainer='Salas leVirve',
  maintainer_email='gae.m.project@gmail.com',
  license='GPLv3',
  packages=['hidemypython'],
  requires=['requests'],
  entry_points={
    'console_scripts': ['hidemypython=hidemypython.cli:main'],
  },
  zip_safe=False
)
