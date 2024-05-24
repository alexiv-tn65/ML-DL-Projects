# пример модульного теста для проверки работы алгоритма анализа тональности текста
import pytest

from ml.model import Prediction, load_model

# Фикстура (fixture) в тестировании представляет собой ресурсы или данные, 
# которые могут быть предварительно настроены и подготовлены для использования 
# в тестах. Она позволяет обеспечить изоляцию тестов и повторное использование 
# кода для подготовки окружения тестирования.
@pytest.fixture(scope="function")
def model():
    # Load the model once for each test function
    return load_model()


# test_sentiment является тестовой функцией, которая использует параметризацию.
# принимает три аргумента: model (загруженная модель), text (текст для анализа) и expected_label (ожидаемая метка тональности).
# Каждый набор данных (text, expected_label) из параметризации запускает эту функцию тестирования,
# где модель используется для анализа текста, а затем проверяется, что предсказанная метка соответствует ожидаемой метке.
@pytest.mark.parametrize(
    "text, expected_label",
    [
        ("очень плохо", "negative"),
        ("очень хорошо", "positive"),
        ("по-разному", "neutral"),
    ],
)
def test_sentiment(model, text: str, expected_label: str):
    model_pred = model(text)
    assert isinstance(model_pred, Prediction)
    assert model_pred.label == expected_label
