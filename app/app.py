from typing import Union
from fastapi import FastAPI, APIRouter
from mangum import Mangum
from fastapi.responses import JSONResponse
import uvicorn
app = FastAPI()
router = APIRouter()
@router.get("/")
def read_root():
    return {"Welcome to": "My first FastAPI deployment using Docker image"}
@router.get("/{text}")
def read_item(text: str):
    return JSONResponse({"result": text})
@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return JSONResponse({"item_id": item_id, "q": q})
app.include_router(router)
handler = Mangum(app)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)