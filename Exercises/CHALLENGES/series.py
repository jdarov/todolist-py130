class Series:

    def __init__(self, digits):
        self._digits = [int(num) for num in digits]
        self._length = len(digits)

    def slices(self, slice_length):
        if not (slice_length <= self._length and slice_length > 0): 
            raise ValueError(
                f"Slice length {slice_length} must be greater than 0 and less than or equal to {self._length}"
                )
        return [
                self._digits[x:x + slice_length] for x in range(0, self._length - slice_length + 1)
                ]