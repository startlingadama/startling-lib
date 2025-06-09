import pytest
from startling_lib import Competence
from pydantic import BaseModel

def test_competence():
    competence = Competence()
    profile = competence.get()
    assert isinstance(profile,BaseModel)
    
    print("test competence passé avec success.")

if __name__ == "__main__":
    test_competence()