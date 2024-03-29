#!/usr/bin/env python3

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class PersonIntel(BaseModel):
	summary:str = Field(description="Summary of the person")
	facts:List[str] = Field(description="Interesting facts about the person")
	topics_of_interest:List[str] = Field(description="Topics that may interest the person")
	ice_breakers: List[str] = Field(description="Create ice breakers to open a conversation with the person")