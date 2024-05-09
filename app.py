#may need to scrap this
#decide between django vs FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
async def chat(request: ChatRequest):
    ai_response = f"Echo: {request.message}"
    return {"response": ai_response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
