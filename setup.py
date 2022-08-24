from setuptools import find_packages
from setuptools import setup

with open("requirements.txt" , mode = "r+" , encoding = "utf-8") as f:
    content = f.readlines()

requirements = [f.strip("\n") for f in content]

setup(name='mylovelypackage',
      version="0.0.1",
      description="Just another lovely project...",
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
