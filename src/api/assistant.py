# to do: fix agent.py and prompt.py to work with joker
import os
import json

from fastapi import APIRouter, Form, status

from src.services.twilio.twilio import send_message
from src.schemas.user_message import UserMessageInSchema
from src.services.llm.agent import ask_assistant

router = APIRouter(tags=["assistant"])


""" @router.post("/assistant-message", status_code=status.HTTP_200_OK)
async def ask(obj_in: UserMessageInSchema):
    resp = await ask_assistant(obj_in.message)
    return resp """


@router.post("/assistant-message", status_code=status.HTTP_200_OK)
async def ask_clara(
    Body: str = Form(default=None),
    From: str = Form(),
    ProfileName: str = Form(),
    MediaUrl0: str = Form(default=None),
):
    "Asks Clara a question regarding Simplicar"
    print("FROM: ", From)
    resp = await ask_assistant(
        json.dumps(
            {
                "human_message": Body.lower() if Body else "",
                "wa_id": From,
                "wa_name": ProfileName,
                "timestamp": "1",
                "image_url": MediaUrl0,
            }
        )
    )
    return send_message(resp, From)
