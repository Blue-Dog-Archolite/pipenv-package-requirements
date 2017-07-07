# Intent

[Pipenv](http://docs.pipenv.org/en/latest/) is a great python virtual environment management system. However it does not have the same popularity as others such as `virtualenv`. This causes some issuesj
when working with a team. Pipenv does not have a native set of tools for making cross virtual environment management tools work nor should it. 

This is a package that allows for a few convince commands in order to provide easier usage for mixed environment teams.


## Tools included

### Rebuilding Requirements

  Rebuilding your requirements file is a pain if it is not your primary source of `pip` truth. This command runs `pipenv lock` and then packages only the non-development
  modules. It also sorts your `requirements.txt` file in alphabetical order for easier reading. 

    $ rebuild_requirements

### Installing packages from Requirements

  Installing from `requirements.txt` file is sometimes required. Pipenv does not provide a quick way to do this. 

    $ install_requirements

  This will process your `requirements.txt` file and install all missing packages to the non-development package set on Pipenv. There is a suggested work around that also
  provides this functionality if you wish to execute it yourself without the necessity of installing this package. 

    $ pipenv install $(< requirements.txt)
