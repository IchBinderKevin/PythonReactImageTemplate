from pydantic import BaseModel


class ExampleResponse(BaseModel):
    """
    Model representing the response for an example item.
    """
    id: int
    name: str

    # Necessary for ORM -> Pydantic model conversion
    # Pydantic expects a dict but SQLAlchemy returns an object,
    # so this allows Pydantic to read attributes from the object (getattr)
    class Config:
        from_attributes = True

class ExampleCreate(BaseModel):
    """
    Model representing the data required to create an example item.
    """
    name: str

class ExampleUpdate(BaseModel):
    """
    Model representing the data required to update an example item.
    """
    id: int
    name: str
