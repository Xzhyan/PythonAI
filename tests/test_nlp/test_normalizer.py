from src.nlp.normalizer import normalize


def test_normalize():
    text = "Meu AmIgo Zé! "

    assert normalize(text) == "meu amigo ze!"
