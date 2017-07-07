#!/usr/bin/env python

import os

from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

"""
This is a generation file that uses pipenv to regenerate the requirements file.
This tool allows for development only requirements that each developer can use separate of the
production tool set.

http://docs.pipenv.org/en/latest/
"""


def rebuild():
    os.system('pipenv lock')
    packages = Project().parsed_pipfile.get('packages', {})
    deps = convert_deps_to_pip(packages, r=False)

    with open('requirements.txt', 'w') as f:
        print(deps)
        f.write('\n'.join(sorted(deps)))


def install():
    os.system('pipenv install $(< requirements.txt)')
