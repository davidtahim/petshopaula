from dataclasses import dataclass,asdict
from typing import Optional

@dataclass
class Cliente:
    id: Optional[int]
    nome: str
    email: str
    telefone: str
    def to_dict(self):
        return asdict(self)
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            nome=data["nome"],
            email=data["email"],
            telefone=data["telefone"]
        )