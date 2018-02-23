from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Ciara Dillon", 
      author_email="ciara.dillon1@ucdconnect.ie",
      license="GPL3",
      packages=['SystemInfo'],
      entry_points={
          'console_scripts':['software_engineering_workspace_systeminfo=SystemInfo.main:main']
          }
      ) 
