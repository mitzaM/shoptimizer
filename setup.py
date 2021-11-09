from setuptools import setup, find_packages

setup(
    name='shoptimizer_api',
    version='1.0',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'flask==1.1.1',
        'requests>=2.22.0',
        'absl-py==0.9.0',
        'mecab-python3==0.996.5',
        'jaconv==0.2.4',
    ],
)
