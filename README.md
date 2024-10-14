# FastAPI App

## Project Structure
```
fastapi_app/
├── app/
│   ├── api/
│   │   └── routes/
│   │        └── items.py                # API routes for item management
│   ├── controllers/
│   │   └── item_controller.py           # Controller logic for handling items
│   ├── core/
│   │   └── config.py                    # Configuration settings (optional)
│   ├── models/
│   │   └── item.py                      # Database model for Item
│   ├── persistence/
│   │   └── base.py                      # Base class for SQLAlchemy models
│   │   └── database.py                  # PostgreSQL database connection and queries
│   │   └── memory.py                    # In-memory storage logic
│   ├── schemas/
│   │   └── item.py                      # Pydantic models (schemas)
│   ├── services/
│   │   └── item_db_service.py           # Services to interact with the database
│   │   └── item_memory_service.py       # Services to interact with in-memory storage
│   └── main.py                          # Main FastAPI app
├── .env                                 # Environment variables
├── README.md                            # Project documentation (this file)
└── Requirements.txt                     # project dependencies
```
---------------------
1. Clone the github repository
```
git clone https://github.com/satpal82bhandari/fastapi-demo.git
cd fastapi-app
```

2. Set up a Python virtual environment and install dependencies
```
python --version
# or
python3 --version
conda search "^python$"
conda create --name env_name python=3.10
conda activate env_name
pip install -r requirements.txt
```

3. Using PostgreSQL as the storage, ensure that the database is created
```
psql -U <username> -d <database_name> -h localhost -W
# OR
createdb <database_name>
```
4. Create a .env file in the root directory and copy format from .env.example
```
STORAGE_TYPE="database"    # Set to "database" or "memory"
DATABASE_URL=postgresql://<username>:<password>@localhost/<database_name>
```
5. Start the FastAPI application using Uvicorn
```
uvicorn app.main:app --reload
```

### API Endpoints

#### Create an Item

```
POST 
http://localhost:8000/items/

Request Body:
{
    "name": "Sample Item",
    "description": "This is a sample item"
}
```
#### Get an Item by ID (DB mode only)
```
GET 
http://localhost:8000/items/{item_id}
```

#### Get All Items (in-memory mode only)
```
GET 
http://localhost:8000/items/memory/
```
### Switching Between Database and In-Memory Storage
Modify the STORAGE_TYPE variable in the .env file:

**For database storage: STORAGE_TYPE="database"**

**For in-memory storage: STORAGE_TYPE="memory"**

Restart the server to apply changes.