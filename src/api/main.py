from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/solve/echo")
def echo(ciphertext: str) -> dict:
    return {"ciphertext": ciphertext}

@app.get("/api/solve/en")
def solve_env(ciphertext: str) -> dict:
    plaintext = "test"
    return {"ciphertext": ciphertext, "plaintext": plaintext}
