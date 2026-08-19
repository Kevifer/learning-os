from fastapi import FastAPI

app = FastAPI(title="Learning OS")


@app.get("/")
def root():
    return {
        "message": "Learning OS is alive!"
    }
