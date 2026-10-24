
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated
from fastapi.responses import JSONResponse

app = FastAPI()


class BMIRequest(BaseModel):
    name: str = Annotated[str, Field(..., min_length=1, max_length=100)]
    weight: float = Annotated[float, Field(..., gt=0, le=500, description="Weight in kilograms")]
    height: float = Annotated[float, Field(..., gt=0, le=300, description="Height in centimetres")]


@app.post("/bmi")
def calculate_bmi(user: BMIRequest):
    height_m = user.height / 100
    bmi = user.weight / (height_m ** 2)
    bmi = round(bmi, 1)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    return {
        "name": user.name,
        "bmi": bmi,
        "category": category,
        "message": f"{user.name}, your BMI is {bmi} and your category is {category}."
    }
