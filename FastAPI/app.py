from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import QAC_Task1_library

app = FastAPI()

class ResultBase(BaseModel):
    k: int
    list_n: List[int]  # Specify the type of elements in the list
    k_exist: bool
    step1: int
    list_nk: List[int]  # Specify the type of elements in the list
    step2: int

origins = ["http://127.0.0.1:3000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def index():
    return {"Msg": "Hello Quan"}

@app.get("/n/{number}", response_model=ResultBase)
async def Get_Result(number: int):
    output1 = QAC_Task1_library.Doing_Everything(number)
    finalresult = ResultBase(
        k=output1['k'],
        list_n=output1['list_n'],
        k_exist=output1['k_exist'],
        step1=output1['step1'],
        list_nk=output1['list_nk'],
        step2=output1['step2']
    )
    
    return finalresult
