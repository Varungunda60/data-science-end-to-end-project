from setuptools import find_packages,setup
from typing import List

def get_requirment(file_path:str)->List[str]:
    requirments =[]
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n","") for req in requirments]
        if "-e ." in requirments:
            requirments.remove("-e .")  
    return requirments  
    

setup(
name='end-to-end-data-science-project',
version='0.0.1',
author='varun',
author_email="varun.gunda01@gmail.com",
packages=find_packages(),
install_requires=get_requirment('requirements.txt')
)
