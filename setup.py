# -*- coding: utf-8 -*-
"""setup.py description.

This is a setup.py template for any project.

"""

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='ecs289-dl-hw',
    version='1.0.0',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',  # GitHub link.
    author='Fangzhou Li',
    author_email='fzli@ucdavis.edu',
    classifiers=[
        'Development Status :: 1 - Planning',
        # 'Environment ::',
        # 'Framework ::',
        # 'Intended Audience ::',
        # 'License ::',
        # 'Natural Language ::',
        # 'Operating System ::',
        # 'Programming Language ::',
        # 'Topic ::',
    ],
    keywords='',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'scikit-learn>=0.23'
        'tensorflow>=2.3',
        'notebook'
    ]
)
