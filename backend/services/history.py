from backend.database.models import SummaryRecord
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_history(user_id: str, db: AsyncSession):
    results = await db.execute(select(SummaryRecord).where(SummaryRecord.user_id == user_id))
    records = results.scalars().all()
    return records