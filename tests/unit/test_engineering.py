from startling_lib import Experience, Profil, EngineerAI
from pydantic import BaseModel
import pytest

@pytest.fixture
def engineer():
    return EngineerAI()

def test_experience():
    experience = Experience()
    assert isinstance(experience.model_dump(), dict)

def test_profil():
    profil = Profil(experiences=[])
    assert profil.model_dump()

def test_engineer_ai():
    e = EngineerAI()
    assert isinstance(e.get_profil(), BaseModel)  # ou BaseModel si vraiment générique

def test_engineer_profil(engineer):
    profil = engineer.get_profil()
    assert isinstance(profil, Profil)