from rasa.nlu.tokenizers.tokenizer import Tokenizer


class MyWhitespaceTokenizer(Tokenizer):
    def __init__(self, component_config):
        super().__init__(component_config)

    def tokenize(self, message, attribute):
        text = message.get(attribute)

        words = text.split()

        tokens = self._convert_words_to_tokens(words, text)

        return self._apply_token_pattern(tokens)
