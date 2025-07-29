class BeerSong:

    _BOTTLE_PHRASES = {
        0: "no more bottles",
        1: "1 bottle"
    }

    @classmethod
    def _bottle_phrase(cls, n):
        return cls._BOTTLE_PHRASES.get(n, f"{n} bottles")

    @classmethod
    def verse(cls, number: int) -> str:
        if number == 0:
            return (
                "No more bottles of beer on the wall, no more bottles of beer.\n"
                "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
            )

        current = cls._bottle_phrase(number)
        next_bottles = cls._bottle_phrase(number - 1)
        action = (
            "Take it down and pass it around" if number == 1
            else "Take one down and pass it around"
        )

        return (
            f"{current.capitalize()} of beer on the wall, {current} of beer.\n"
            f"{action}, {next_bottles} of beer on the wall.\n"
        )

    @classmethod
    def verses(cls, start: int, end: int) -> str:
        return "\n".join(cls.verse(n) for n in range(start, end - 1, -1))

    @classmethod
    def lyrics(cls) -> str:
        return cls.verses(99, 0)
