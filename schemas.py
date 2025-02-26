from pydantic import BaseModel, Field

class BookSchema(BaseModel):
    title: str = Field(min_length=3, description="The title of the book",)
    author: str = Field(min_length=3, description="The author of the book")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "The Great Gatsby", 
                "author": "F. Scott Fitzgerald"
            }
        }
    }