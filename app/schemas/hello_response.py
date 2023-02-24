from pydantic import BaseModel


class HelloResponse(BaseModel):
    hello: str
