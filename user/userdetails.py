from typing import Type
from user.degree import Degree
from user.certificate import Certificate
from user.language import Language


class UserDetails:
    def __init__(
        self,
        location: dict,
        skills: list[str],
        degrees: list[Type[Degree]],
        certificates: list[Type[Certificate]],
        language: list[Type[Language]]
    ):
        self.location = location
        self.skills = skills
        self.degrees = degrees
        self.certificates = certificates
        self.language = language
