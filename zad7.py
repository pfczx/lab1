import argparse
import requests
from pydantic import BaseModel


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    address_1: str | None = None
    address_2: str | None = None
    address_3: str | None = None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: float | None = None
    latitude: float | None = None
    phone: str | None = None
    website_url: str | None = None
    state: str
    street: str | None = None

    def __str__(self):
        return (
            f"Browar: {self.name} (id: {self.id})",
            f"  Typ:        {self.brewery_type}",
            f"  Adres:      {self.street or self.address_1 or '-'}, "
            f"{self.postal_code} {self.city}, {self.state}, {self.country}",
            f"  Telefon:    {self.phone}"
            f"  Strona:     {self.website_url}"
            f"  Współrzędne: {self.latitude}, {self.longitude}")


parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str, default=None)
args = parser.parse_args()

url = "https://api.openbrewerydb.org/v1/breweries/"
params = {"per_page": 20}
if args.city:
    params["by_city"] = args.city

data = requests.get(url, params=params).json()[:20]

for element in data:
    print(element)
    print("\n")
