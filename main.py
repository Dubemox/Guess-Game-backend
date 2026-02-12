from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

origins = [
    "http://guess-game-frontend-zeta.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

secret_number = random.randint(1, 10)
attempts = 5

@app.post("/guess")
def guess_number(data: dict):
    global attempts, secret_number

    guess = int(data["guess"])

    if guess == secret_number:
        secret_number = random.randint(1, 10)
        attempts = 5
        return {"message": "🎉 Correct!", "attempts": attempts}

    attempts -= 1

    if attempts == 0:
        answer = secret_number
        secret_number = random.randint(1, 10)
        attempts = 5
        return {"message": f"😭 Game over! Number was {answer}", "attempts": attempts}

    if guess < secret_number:
        return {"message": "Too low ⬇️", "attempts": attempts}

    return {"message": "Too high ⬆️", "attempts": attempts}
