# Guide on how to create a migration

## Step 1: Be sure the database exists and is up to date
To do this you can run the following command:

```bash
cd backend
uv run python src/main.py # this creates the folders and db file if not existing
alembic upgrade head
```

## Step 2a: Create a new migration
If using automatic generation, create a new domain model inheriting from Base and import it in the __init__.py.
The __init__.py import is necessary so alembic can find the model during autogeneration.

Then run the following command to create a new migration:

X = next revision ID, e.g. 001, 002, 003, etc. You can also use a custom revision ID if you want, but it should be unique and not conflict with existing revisions.
The rev_id can be omitted and alembic will generate a random one, but I prefer to have them in order and easily identifiable.
```bash
cd backend
alembic revision --autogenerate -m "migration message" --rev-id 00X
```
After generating CHECK(!) the generated migration file in backend/src/database/migrations/versions/ to make sure it looks correct and doesn't contain any unwanted changes. If it does, you can edit the file manually to fix it.

## Step 2b: Create a new migration manually
If you prefer to write the migration manually, you can run:

```bashcd backend
alembic revision -m "migration message" --rev-id 00X
```
and then manually add commands either via sqlalchemy command or raw sql (op.execute("RAW SQL")) in the generated file

## Step 3: Apply the migration
To apply the migration to the database, run the following command:
```bash
cd backend
alembic upgrade head
```
The docker container uses an entrypoint that runs this command automatically on startup.