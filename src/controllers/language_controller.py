from flask import Blueprint, request, render_template
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator
from models.history_model import HistoryModel

language_controller = Blueprint("language_controller", __name__)


def translate_and_save(
    text_to_translate, translate_from, translate_to, reverse=False
):
    translated = GoogleTranslator(
        source=str(translate_from), target=str(translate_to)
    ).translate(str(text_to_translate))

    HistoryModel(
        {
            "text_to_translate": translated if reverse else text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to,
        }
    ).save()

    return translated


@language_controller.route("/", methods=["GET", "POST"])
def language_list():
    languages = LanguageModel.list_dicts()

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        translated = translate_and_save(
            text_to_translate, translate_from, translate_to
        )

    else:
        text_to_translate = (
            request.form.get("text-to-translate") or "O que deseja traduzir?"
        )

        translate_from = request.form.get("translate-from") or "pt"
        translate_to = request.form.get("translate-to") or "en"
        translated = "What do you want to translate?"

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@language_controller.route("/reverse", methods=["POST"])
def reverse_translate():
    languages = LanguageModel.list_dicts()

    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    translated = translate_and_save(
        text_to_translate, translate_from, translate_to
    )

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
