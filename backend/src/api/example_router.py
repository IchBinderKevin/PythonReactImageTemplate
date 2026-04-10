from fastapi import APIRouter, status, HTTPException, Response

from models.schema.example import ExampleCreate, ExampleUpdate
from services import example_service


def create_example_router():
    """
    Creates the example router.
    """
    router = APIRouter()

    @router.post("/add")
    async def add_example(example: ExampleCreate):
        """
        Simple endpoint to add a db example entry.
        """
        try:
            await example_service.add_example(example)
            return Response(status_code=status.HTTP_200_OK)
        except ValueError as e:
            raise HTTPException(400, str(e))

    @router.post("/update")
    async def edit_tag(example: ExampleUpdate):
        """
        Simple endpoint to update a db example entry.
        """
        try:
            await example_service.update_example(example)
            return Response(status_code=status.HTTP_200_OK)
        except ValueError as e:
            raise HTTPException(400, str(e))

    @router.delete("/delete/{example_id}")
    async def delete_example(example_id: int):
        """
        Simple endpoint to delete example entry.
        """
        try:
            await example_service.delete_example(example_id)
            return Response(status_code=status.HTTP_200_OK)
        except ValueError as e:
            raise HTTPException(400, str(e))

    @router.get("/list")
    async def list_examples():
        """
        Simple endpoint to list example entries.
        """
        try:
            return await example_service.list_examples()
        except ValueError as e:
            raise HTTPException(400, str(e))

    return router
