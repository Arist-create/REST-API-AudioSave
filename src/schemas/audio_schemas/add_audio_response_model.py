from pydantic import BaseModel


class AddAudioResponseModel(BaseModel):
    url: str