from pydantic import BaseModel, Field


class FLowTicketModel(BaseModel):
    page: int = Field(1, description="页数")
    page_size: int = Field(10, description="每页个数")


class SearchBusinessModel(BaseModel):
    start: int = Field(1, description="页数")
    limit: int = Field(10, description="每页个数")
