# module_4/main_exercise/e2e/screenplay/actor.py
from typing import Any, Dict, Type

class Actor:
    def __init__(self, name: str):
        self.name = name
        self._abilities: Dict[Type, Any] = {}

    # Fábricas (elige la que prefieras usar en tus fixtures)
    @staticmethod
    def named(name: str) -> "Actor":
        return Actor(name)

    @staticmethod
    def name(name: str) -> "Actor":
        # alias por si en algún sitio quedó Actor.name("...")
        return Actor.named(name)

    # ---- Screenplay API ----
    def can(self, ability: Any) -> "Actor":
        """Confiere una habilidad al Actor (p. ej., BrowseTheWeb.using(page))."""
        self._abilities[type(ability)] = ability
        return self

    def ability_to(self, ability_type: Type) -> Any:
        ability = self._abilities.get(ability_type)
        if not ability:
            raise RuntimeError(f"{self.name} no tiene la habilidad {ability_type.__name__}")
        return ability

    def attempts_to(self, *tasks_or_interactions):
        """Ejecuta Tasks/Interactions que implementen `.performed_by(actor)`."""
        for t in tasks_or_interactions:
            t.performed_by(self)

    def should(self, *questions):
        """Evalúa Questions que implementen `.answered_by(actor)` (con asserts dentro)."""
        for q in questions:
            q.answered_by(self)