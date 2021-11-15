#!/usr/bin/env python3

import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'src', '__version__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)

requirements = []
with open(os.path.join(here, 'requirements.txt'), 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')

        if line:
            requirements.append(line)

readme = ""
if os.path.exists(os.path.join(here, 'README.md')):
    with open(os.path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
        readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=[about['__title__']] + [f'{about["__title__"]}.{x}' for x in find_packages(os.path.join(here, 'src'), exclude=["test"])],
    package_data={},
    package_dir={about['__title__']: 'src'},
    include_package_data=True,
    python_requires=">=3.8.0",
    install_requires=requirements,
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={},
    tests_require=[],
    extras_require={},
    project_urls={
        'Documentation': about['__url__'],
        'Source': about['__url__']
    }
)
