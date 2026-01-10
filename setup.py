# Find_packages will automatically find all the packages which are available in the entire machine learning project


from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT='-e .'


def get_requirments(file_path:str)->List[str]:
    '''
    This function will return the list of requirments
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)

    return requirments



setup(
    name="Diamond project predictor",
    #If we release any new version we will simply change this
    version="0.0.1",
    author="Mujahid U.K. Afridi",
    author_email="mujahidkafridi@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')   # As we have 100s of libraries so its not good to write in []. It will take packages from requirments file
)