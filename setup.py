from setuptools import find_packages, setup
from typing import List

# -e . del requirements
GUION_E_PUNTO = '-e .'
# Funcion para instalar todas las librerias
def get_requirements(file_path:str )->List[str]:
    '''
    Esta funcion devuelve la lista de requeriments
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # eliminar las n/ del readlines
        requirements = [req.replace("\n", "") for req in requirements]

        if GUION_E_PUNTO in requirements:
            requirements.remove(GUION_E_PUNTO)
    
    return requirements
setup(
name='mlproject',
version='0.0.1',
author='Felipe',
author_email='ing.fzuniga@gmail.com',
packages = find_packages(),
install_requirements = get_requirements('requirements.txt')

)