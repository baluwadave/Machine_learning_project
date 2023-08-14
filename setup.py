# from setuptools import find_packages , setup
# #from typing import List
# hypen_e_dot = '-e .'

# def get_requiremnets(file_path:str)->list[str]:
#     """
#     this funcion will return the list of requirement
#     """
#     requirments=[]
#     with open(file_path)as file_obj:
#         requirments=file_obj.readlines()
#         requirments=[req.replace("\n"," ")for req in requirments]
#         if hypen_e_dot in requirments:
#             requirments.remove(hypen_e_dot)
#     return requirments        


# setup(
#     name = 'Machine learning Project',
#     version='0.0.1',
#     author='BALU',
#     author_email='baluwadave@gmail.com',
#     packages=find_packages(),
#     install_requires=get_requiremnets('requirement.txt')
# )
from setuptools import find_packages, setup


def get_requirements(file_path):
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != '-e.']
    return requirements


setup(
    name='MachineLearningProject',  # Change this to your project name
    version='0.0.1',
    author='BALU',
    author_email='baluwadave@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Make sure your requirements file is named 'requirements.txt'
)
