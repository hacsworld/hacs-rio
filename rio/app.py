from fastapi import FastAPI
app = FastAPI()

@app.get('/ui')
async def ui():
    return {"msg": "RIO orchestrator running"}
