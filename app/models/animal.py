from dataclasses import dataclass,asdict
from typing import Optional

@dataclass
class Animal:
    id: Optional[int]
    nome: str
    raca: str
    especie: str
    dono_id: int
    idade: int
    def to_dict(self):
        return asdict(self)
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            nome=data["nome"],
            raca=data["raca"],
            especie=data["especie"],
            dono_id=data["dono_id"],
            idade=data["idade"]
        )