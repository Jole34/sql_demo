## Alembic migrations
- Runs migration with the latest model changes  (creates new file inside versions dir)
    ```commandline
    alembic revision --autogenerate -m "Init" 
    ```
- Applies migration to the database
  ```commandline
  alembic upgrade head
  ```
