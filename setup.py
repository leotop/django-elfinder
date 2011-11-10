import os
from setuptools import setup

def read_file(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

setup(
    name = "django-elfinder",
    version = __import__('elfinder').get_version().replace(' ', '-'),
    url = '',
    author = 'unkier',
    author_email = '',
    description = 'Django-elFinder is an easy way to use the elFinder file manager within Django without creating dependencies.',
    long_description = read_file('README.rst'),
    include_package_data = True,
    install_requires=read_file('requirements.txt'),
    classifiers = [
    ],
)
