from collections import Counter


class TextService:
    def process(self, text: str) -> dict:
        words = text.split()
        word_count = Counter(words)
        return {
            "original": text,
            "uppercase": text.upper(),
            "word_count": len(words),
            "frequency": dict(word_count),
        }
