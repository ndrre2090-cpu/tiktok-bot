from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "bot is running"}

@app.post("/webhook")
async def handle_webhook():
    return {"message": "Webhook received"}

