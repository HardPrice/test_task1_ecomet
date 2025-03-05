# FastAPI PostgreSQL Connection Example

This project demonstrates how to set up a FastAPI application with a connection to a PostgreSQL database using `asyncpg` and connection pooling. The application includes an endpoint to fetch the PostgreSQL version.

## Requirements

- Python 3.11+
- FastAPI
- asyncpg
- uvicorn
- pydantic

## Setup

1. Clone the repository:

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/0) file in the project root with your database configuration:

    ```env
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=your_user
    DB_PASSWORD=your_password
    DB_NAME=your_database
    ```

5. Run the application:

    ```sh
    uvicorn main:create_app --factory
    ```

## Endpoints

- **GET /api/db_version**: Fetches the PostgreSQL version.

## Project Structure

- [main.py](http://_vscodecontentref_/1): Main application file with FastAPI setup and route registration.
- [config.py](http://_vscodecontentref_/2): Configuration file for loading environment variables using `pydantic`.

## Notes

- The application uses connection pooling provided by [asyncpg](http://_vscodecontentref_/3) to manage database connections efficiently.
- Error handling is implemented to ensure that database connection errors are properly managed and reported.

## License

This project is licensed under the MIT License.