from typing import Type
from user_profile.degree import Degree
from user_profile.certificate import Certificate


class Profile:
    def __init__(
        self,
        location: str,
        skills: list[str],
        degrees: list[Type[Degree]],
        certificates: list[Type[Certificate]],
        languages: list[str],
    ):
        self.location = location
        self.skills = skills
        self.degrees = degrees
        self.certificates = certificates
        self.languages = languages
