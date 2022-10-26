from itertools import permutations
from typing import List

from fastapi import Body, FastAPI


app = FastAPI()

@app.post("/pair-of-numbers")
async def pair_of_numbers(sum_: int, list_: List[int] = Body()):
    for pair in permutations(list_, 2):
        if sum(pair) == sum_:
            return {"result": pair} 
    return {"result": None} 

    
