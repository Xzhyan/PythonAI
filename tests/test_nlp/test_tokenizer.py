from src.nlp import tokenize


def test_tokenize():
    text = "eu tenho 25 anos!"

    assert tokenize(text) == ['eu', 'tenho', '25', 'anos', '!']
    