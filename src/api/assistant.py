# to do: fix agent.py and prompt.py to work with joker
import os
from fastapi import APIRouter, status

from src.schemas.user_message import UserMessageInSchema
from src.services.llm.agent import ask_assistant

router = APIRouter(tags=["assistant"])

@router.post("/assistant-message", status_code=status.HTTP_200_OK)
async def ask(obj_in: UserMessageInSchema):
    """Ask assistant"""
    resp = await ask_assistant(obj_in.message)
    return resp

