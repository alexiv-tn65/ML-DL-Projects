from dataclasses import dataclass
from pathlib import Path

import yaml
from transformers import pipeline

# load config file
config_path = Path(__file__).parent / "config.yaml"
with open(config_path, "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


@dataclass
class Prediction:
    """prediction result"""

    label: str # Метка тональности
    score: float # Оценка тональности


def load_model():

    model_hf = pipeline(config["task"], model=config["model"], device=-1) # Загрузка модели NLP

    def model(text: str) -> Prediction:
        pred = model_hf(text) # Предсказание тональности
        pred_best_class = pred[0] # Выбор наилучшего класса
        return Prediction(
            label=pred_best_class["label"], # Метка тональности
            score=pred_best_class["score"],
        )

    return model # Возвращение функции модели
