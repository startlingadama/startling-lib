import pytest
from startling_lib import Competence,Personal
from pydantic import BaseModel

@pytest.fixture
def personal():
    return Personal()


def test_competence():
    competence = Competence()
    profile = competence.get()
    assert isinstance(profile,BaseModel)
    
    print("test competence passé avec success.")

def personal_test():

    assert personal.firstname == "Adama" and personal.lastname == "COULIBALY"
