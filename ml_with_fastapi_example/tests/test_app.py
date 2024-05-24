import pytest
import requests


# декоратор позволяет определить параметризованный тест. 
# Он принимает список значений для входных данных и ожидаемых 
# результатов и выполняет тесты для всех комбинаций значений.
@pytest.mark.parametrize(
    "input_text, expected_label",
    [
        ("очень плохо", "negative"),
        ("очень хорошо", "positive"),
        ("по-разному", "neutral"),
    ],
)
def test_sentiment(input_text: str, expected_label: str):
    response = requests.get("http://0.0.0.0/predict/", params={"text": input_text}) # отправляет GET-запрос на указанный URL
    assert response.json()["text"] == input_text # проверяет, что текст, возвращенный в ответе JSON, соответствует входному тексту
    assert response.json()["sentiment_label"] == expected_label 
