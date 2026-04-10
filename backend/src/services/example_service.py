"""
example service with simple CRUD operation examples.
"""
from database.db import AsyncSessionLocal
from sqlalchemy.exc import IntegrityError
from sqlalchemy import  select, delete

from models.domain.example import Example
from models.schema.example import ExampleResponse, ExampleCreate, ExampleUpdate


async def add_example(example_create: ExampleCreate) -> int:
    """
    Adds a new example item to the database.
    :param example_create: The ExampleCreate model containing the name of the example item to create.
    :return: The id of the newly created example item.
    """
    if example_create.name.strip() == "":
        raise ValueError("Tag name cannot be empty.")

    async with AsyncSessionLocal() as session:
        example = Example(name=example_create.name.strip())
        session.add(example)
        try:
            await session.commit()
        except IntegrityError:
            await session.rollback()
            raise ValueError(f"'{example}' already exists.")
        await session.refresh(example)
        return example.id

async def update_example(example_update: ExampleUpdate):
    """
    Updates the name of an existing example item in the database.
    :param example_update: The ExampleUpdate model containing the id of the example item to update and the new name.
    """
    if example_update.name.strip() == "":
        raise ValueError("Tag name cannot be empty.")
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Example).where(Example.id == example_update.id)
        )
        existing_example = result.scalars().first()

        if existing_example is None:
            raise ValueError(f"ID '{example_update.id}' does not exist.")

        existing_example.name = example_update.name.strip()
        await session.commit()

async def delete_example(example_id: int):
    """
    Deletes an example item from the database by its ID.
    :param example_id: The id to delete.
    """
    async with AsyncSessionLocal() as session:
        result = await session.execute(delete(Example).where(Example.id == example_id))
        if result.rowcount == 0:
            raise ValueError(f"'{example_id}' does not exist.")
        await session.commit()

async def list_examples() -> list[ExampleResponse]:
    """
    Lists all example items in the database.
    :return:
    """
    async with AsyncSessionLocal() as session:
        res =  (await session.scalars(select(Example))).all()
        return [ExampleResponse.model_validate(r) for r in res]
