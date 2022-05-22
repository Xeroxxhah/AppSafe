from setuptools import setup, find_packages
import codecs
import os

if os.geteuid() != 0:
    print('Run it as root')
    quit()

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.4.1'
DESCRIPTION = 'A Simple python AppLocker and FileLocker'
LONG_DESCRIPTION = 'A Simple python AppLocker and FileLocker'

# Setting up
setup(
    name="AppSafe",
    version=VERSION,
    author="Xeroxxhah (Muhammad Nauman Azeem)",
    author_email="xeroxxhah@pm.me",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['easygui', 'pyAesCrypt'],
    keywords=['python', 'python3', 'FileLock', 'AppLock','linux',],
    classifiers=[
        "Development Status :: Running",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ],
    entry_points="""
    [console_scripts]
    appsafe=AppSafe.appsafe:main
    """,
)
