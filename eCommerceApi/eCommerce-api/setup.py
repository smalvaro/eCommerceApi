import io
from setuptools import setup, find_packages


def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            yield line.strip()


setup(
    name='eCommerce-api',
    version='1.0',
    packages=find_packages(),
    url="https://github.com/smalvaro",
    author='Álvaro Sánchez Moro',
    author_email='smalvaro@usal.es',
    description='',
    long_description_content_type='text/markdown',
    install_requires=requirements(filename='requirements.txt'),
    data_files=[],
    entry_points={
        'console_scripts': [
            'eCommerce-api=eCommerce_api.run:main'
        ],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers"
    ],
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/smalvaro',
        'Source': 'https://github.com/smalvaro',
    },
)