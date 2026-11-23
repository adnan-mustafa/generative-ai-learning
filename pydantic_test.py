import truststore
truststore.inject_into_ssl()

from pydantic import BaseModel, Field, ValidationError

class Movie(BaseModel):
    title: str
    year: int

print(Movie(title="Inception",year="2010"))

try:
    Movie(title=2010,year=2010)
except ValidationError as error:
    print(error)