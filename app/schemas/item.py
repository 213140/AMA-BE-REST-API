from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=5000)

class ItemUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=5000)

class ItemPublic(BaseModel):
    id: int
    title: str
    description: str | None
    owner_id: int

    model_config = {"from_attributes": True}
