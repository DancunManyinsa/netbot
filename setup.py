import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
   name="netbot",
   version="0.0.1",
   description="Network monitoring bot",
   long_description=read("README.md"),
   author="Kazuki Yokoyama",
   author_email="kmyokoyama@inf.ufrgs.br",
   url="https://github.com/kmyokoyama/netbot",
   packages=["netbot"],
   install_requires=["pyspeedtest"],
   test_suite="tests"
)
