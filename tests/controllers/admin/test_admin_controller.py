from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
# from bson import ObjectId


def test_history_delete(app_test):
    user = UserModel(
        {"name": "Dan", "level": "admin", "token": "matilda"}
    ).save()
    admin_token = user.data["token"]
    admin_username = user.data["name"]

    history = HistoryModel({
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "pt",
    }).save()

    response = app_test.delete(
        f"/admin/history/{history.data['_id']}",
        headers={"Authorization": admin_token, "User": admin_username},
    )

    assert user.token_is_valid(admin_token) is True
    assert response.status_code == 204
    assert HistoryModel.find_one(
        {"text_to_translate": "Hello, I like videogame"}) is None
    assert UserModel.find_one({"name": "Dan"}) is not None
