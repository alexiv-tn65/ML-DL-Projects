from fastapi import FastAPI
from pydantic import BaseModel

from ml.model import load_model

model = None
app = FastAPI()


class Response(BaseModel):
    text: str
    sentiment_label: str
    sentiment_score: float


# Создаем маршрут (route) для главной страницы
# create a route
@app.get("/")
def index():
    return {"text": "Sentiment Analysis"}

# Регистрируем функцию для выполнения во время запуска приложения
# Register the function to run during startup
@app.on_event("startup")
def startup_event():
    global model
    model = load_model()

# Обработчик маршрута для предсказания сентимента
# Your FastAPI route handlers go here
@app.get("/predict")
def predict_sentiment(text: str): # Принимает текст для предсказания
    sentiment = model(text) # Делаем предсказание сентимента на основе загруженной модели

    # Формируем ответ с предсказанным сентиментом
    response = Response(
        text=text,
        sentiment_label=sentiment.label,
        sentiment_score=sentiment.score,
    )

    return response
