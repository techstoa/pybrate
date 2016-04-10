from distutils.core import setup

setup(name='pybrate',
      version='0.2',
      description='Python module for detecting movement',
      author='Gregory Boyce',
      author_email='gregory.boyce@gmail.com',
      url='https://github.com/gdfuego/pybrate',
      py_modules = ['pybrate', 'dryer'],
      scripts=['track_dryer']
      )
