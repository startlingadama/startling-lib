from pydantic import BaseModel, Field

class Experience(BaseModel):
    annee: str = Field(description = "", default = "1 ans")
    post: str = Field(description = "", default = "Developeur/Integrateur ai")
    entreprise: str = Field(description = "", default = "OpenSNZ Technlogies")

class Profil(BaseModel):
    profil: str = Field(description = "" , default = "Ingenieur IA")
    experiences: list[Experience] = Field(description = "", default = [Experience()])

class EngineerAI:

    def __init__(self):
        self.profil: Profil = Profil(experiences=[])

    def get_profil(self) -> Profil:
        return self.profil


