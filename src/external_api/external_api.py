import aiohttp
from aiohttp import client_exceptions

from aiohttp_socks import ProxyConnector

from fastapi import HTTPException, status

from src.external_api.config import external_api_settings
from src.schemas.question import QuestionRequestSchema


async def ask_question(schema: QuestionRequestSchema):
    conn = ProxyConnector.from_url(external_api_settings.PROXY)
    async with aiohttp.ClientSession(trust_env=True, connector=conn) as session:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {external_api_settings.KEY}"
            
        }
        body = {
            "model": external_api_settings.MODEL,
            "messages": [
                {
                    "role": external_api_settings.ROLE,
                    "content": schema.content
                }
            ]
        }
        try:
            async with session.post(
                url=external_api_settings.URL,
                headers=headers,
                json=body,
                ssl=False,
            ) as response:
                response = await response.json()
                return response["choices"][0]["message"]["content"]
        except client_exceptions.ContentTypeError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="ChatGPT service is temporary unavailable"
            )
