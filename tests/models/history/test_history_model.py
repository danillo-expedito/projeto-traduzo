import json
from src.models.history_model import HistoryModel
# from .conftest import prepare_base


# Req. 7
def test_request_history():

    history = json.loads(HistoryModel.list_as_json())

    assert len(history) == 2
    assert history[0]["text_to_translate"] == "Hello, I like videogame"
    assert history[0]["translate_from"] == "en"
    assert history[0]["translate_to"] == "pt"
    assert history[1]["text_to_translate"] == "Do you love music?"
    assert history[1]["translate_from"] == "en"
    assert history[1]["translate_to"] == "pt"
