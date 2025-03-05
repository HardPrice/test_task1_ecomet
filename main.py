from typing import Annotated

import asyncpg
import uvicorn
from fastapi import APIRouter, FastAPI, Depends, HTTPException
from asyncpg.pool import Pool
from config import settings


async def create_pool() -> Pool:
    return await asyncpg.create_pool(
        host=settings.db_host,
        port=settings.db_port,
        user=settings.db_user,
        password=settings.db_password,
        database=settings.db_name,
        min_size=1,
        max_size=10
    )


async def get_pg_connection(pool: Annotated[Pool, Depends(create_pool)]) -> asyncpg.Connection:
    async with pool.acquire() as connection:
        try:
            yield connection
        except Exception as e:
            raise HTTPException(status_code=500, detail="Database connection error") from e


async def get_db_version(conn: Annotated[asyncpg.Connection, Depends(get_pg_connection)]):
    try:
        return await conn.fetchval("SELECT version()")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch database version") from e


def register_routes(app: FastAPI):
    router = APIRouter(prefix="/api")
    router.add_api_route(path="/db_version", endpoint=get_db_version)
    app.include_router(router)


def create_app() -> FastAPI:
    app = FastAPI(title="e-Comet")
    register_routes(app)
    return app


if __name__ == "__main__":
    uvicorn.run("main:create_app", factory=True)