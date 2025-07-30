class Series:

    def __init__(self, digits):
        self._digits = digits
        self._length = len(digits)

    def slices(self, slice_length):
        if slice_length <= self._length and slice_length > 0: 
            return [
                    [int(num) for num in sublist] # convert each string num to an int in each sublist of the slice
                    for sublist in
                    [
                        self._digits[x:x + slice_length] for x in range(0, self._length - slice_length + 1)
                    ] 
            ]
        raise ValueError(f"Slice length {slice_length} must be greater than 0 or less than or equal to length of digits")