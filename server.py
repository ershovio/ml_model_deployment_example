import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# App creation and model loading
app = FastAPI()
model = joblib.load("./model.joblib")


class IrisSpecies(BaseModel):
    """
    Input features validation for the ML model
    """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post('/predict')
def predict(iris: IrisSpecies):
    """
    :param iris: input data from the post request
    :return: predicted iris type
    """
    features = [[
        iris.sepal_length,
        iris.sepal_width,
        iris.petal_length,
        iris.petal_width
    ]]
    prediction = model.predict(features).tolist()[0]
    return {
        "prediction": prediction
    }


if __name__ == '__main__':
    # Run server using given host and port
    uvicorn.run(app, host='127.0.0.1', port=80)
