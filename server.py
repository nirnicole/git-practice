from fastapi import FastAPI
import uvicorn


app = FastAPI()


# server code...
@app.get("/")
async def root():
    return {"message": "Hello World Exercise"}

@app.get("/sanity")
async def sanity():
    return "Server is up and running smoothly"


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
