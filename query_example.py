import requests
from sklearn.datasets import load_iris

# An example to test that the server works correctly.
# It takes one sample for each Iris type, requests prediction and compares it with the right target
if __name__ == '__main__':
    iris = load_iris()
    for i in [0, 50, 100]:
        x = iris.data[i]
        y = iris.target[i]
        features = {
            "sepal_length": x[0],
            "sepal_width": x[1],
            "petal_length": x[2],
            "petal_width": x[3]
        }
        resp = requests.post(
            "http://127.0.0.1:80/predict",
            json=features
        )
        print(f"Input features: {features}")
        print(f"Predicted: {resp.json()}")
        print(f"Expected: {y}")
        print("----")
