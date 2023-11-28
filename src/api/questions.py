from fastapi import APIRouter, Depends, status

from src.external_api.external_api import ask_question
from src.schemas.question import QuestionRequestSchema, QuestionResponseSchema
from src.schemas.token import TokenPayloadSchema
from src.services.questions_service import QuestionsService
from src.token.token import Token


router = APIRouter(
    prefix="/questions",
    tags=["Questions controller"]
)


@router.post("", status_code=status.HTTP_201_CREATED)
async def ask_and_create_question(
    schema: QuestionRequestSchema,
    user_info: TokenPayloadSchema = Depends(Token.verify_token),
    service: QuestionsService = Depends()
):
    await service.create_question(int(user_info.sub), schema)
    answer = await ask_question(schema)
    return answer


@router.get("/me", response_model=list[QuestionResponseSchema])
async def get_last_three_questions(
    user_info: TokenPayloadSchema = Depends(Token.verify_token),
    service: QuestionsService = Depends()
):
    questions = await service.read_last_three_questions(int(user_info.sub))
    return questions


@router.get("", response_model=QuestionResponseSchema)
async def get_question(
    id: int,
    _: TokenPayloadSchema = Depends(Token.verify_admin),
    service: QuestionsService = Depends()
):
    question = await service.read_question(id)
    return question
