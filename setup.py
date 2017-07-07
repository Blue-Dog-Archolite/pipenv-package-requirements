from setuptools import setup

setup(name='pipenv-package-requirements',
      version='0.1',
      description='Pipenv tools for requirements.txt',
      url='https://github.com/Blue-Dog-Archolite/pipenv-package-requirements',
      author='Robert R. Meyer',
      author_email='Blue.Dog.Archolite@gmail.com',
      license='GNU',
      packages=['pipenv_tools'],
      zip_safe=True,
      console_scripts=[
          'rebuild_requirements=pipenv_tools.command_line:rebuild',
          'install_requirements=pipenv_tools.command_line:install',
      ],
      keywords='pipenv virtualenv',
      install_requires=[
          'pipenv',
      ],
      )
