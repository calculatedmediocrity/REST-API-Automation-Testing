class TestExample:
    def test_set_phrase(self):
        phrase = input("Set phrase:  ")
        assert len(phrase) <= 15, "Phrase contain more than 15 symbols"
