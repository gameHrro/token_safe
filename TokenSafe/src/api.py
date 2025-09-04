from fastapi import FastAPI, HTTPException, Depends
from db.database import engine
from db.model import Base
from db.schemes import AddNewTokenSchemes
from db.database import SessionDep
from db.model import TokenModel

app = FastAPI(title='TokenSafe', debug=True)

@app.post('/setup_db/', tags=['📊 База данных'], summary='Устанавливаем соединение с бд')
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all())
        await conn.run_sync(Base.metadata.create_all())

        return {'✅ status': 200}

@app.post('/add_token/', tags=['🔗 Токен'], summary='Добавляем токен в базу')
async def add_token(data: AddNewTokenSchemes, session: SessionDep):
    new_data = TokenModel(
        title=data.title,
        token=data.token,
    )
    
    session.add(new_data)
    await session.commit()

