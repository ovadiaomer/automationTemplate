from enum import Enum
from dataclasses import dataclass

class Company(Enum):
    BANK_HAPOALIM = "520000118"
    # Add other companies as needed

@dataclass
class CompanyData:
    name: Company
    id: str
