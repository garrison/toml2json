try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='toml2json',
    version='0.1dev',
    author='Jim Garrison',
    py_modules=[
        "toml2json",
    ],
    scripts=[
        "scripts/toml2json",
        "scripts/json2toml",
    ],
    install_requires=['toml'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
