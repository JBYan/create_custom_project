from setuptools import setup

setup(
    name='create_project',
    version='0.1',
    py_modules=['create_project'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        create_project=create_project:main
    ''',
)