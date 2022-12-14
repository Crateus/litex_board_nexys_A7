#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages


setup(
    name="litex-boards-nexys_A7",
    description="Add Litex support for Digilent Nexys A7",
    author="Yassine Faize",
    author_email="yfaize@keysom.io",
    #url="http://enjoy-digital.fr",
    download_url="https://github.com/Crateus/litex_board_nexys_A7",
    #test_suite="test",
    #license="BSD",
    python_requires="~=3.6",
    packages=find_packages(),
    package_data={
    	'litex_boards': ['litex_boards/**'],
    },
    include_package_data=True,
    #package_dir={"": "litex-boards"},
)
