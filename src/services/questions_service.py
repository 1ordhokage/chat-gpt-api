from datetime import datetime

from fastapi import Depends, HTTPException, status

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_async_session
from src.models.questions import Question
from src.schemas.question import QuestionRequestSchema


class QuestionsService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
    
    async def read_question(self, id: int) -> Question:
        result = await self.session.execute(
            select(Question)
            .where(Question.id == id)
        )
        question = result.scalar()
        if not question:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found"
            )
        return question
        
    async def read_last_three_questions(self, user_id: int) -> list[Question]:
        questions = await self.session.execute(
            select(Question)
            .where(Question.user_id == user_id)
            .order_by(desc(Question.asked_at))
            .limit(3)
        )
        return questions.scalars()

    async def create_question(
        self,
        user_id: int,
        schema: QuestionRequestSchema
    ) -> None:
        question = Question(
            user_id=user_id,
            content=schema.content,
            asked_at=datetime.now()
        )
        self.session.add(question)
        await self.session.commit()
