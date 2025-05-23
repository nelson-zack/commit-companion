from setuptools import setup

setup(
    name='commit-companion',
    version='1.0.0',
    py_modules=['cli', 'main', 'git_utils', 'ai_utils', 'utils'],
    install_requires=[
        'click',
        'openai',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'commit-companion=cli:cli',
        ],
    },
)