from setuptools import setup, find_packages


setup(
    name='sublime_info',
    version='0.1.0',
    description='Gather information about Sublime Text',
    long_description=open('README.rst').read(),
    keywords=[
        'sublime',
        'sublime text',
        'info',
        'plugin'
    ],
    author='Todd Wolfson',
    author_email='todd@twolfson.com',
    url='https://github.com/twolfson/sublime-info',
    download_url='https://github.com/twolfson/sublime-info/archive/master.zip',
    packages=find_packages(),
    license='UNLICENSE',
    install_requires=open('requirements.txt').readlines(),
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Text Editors'
    ]
)
