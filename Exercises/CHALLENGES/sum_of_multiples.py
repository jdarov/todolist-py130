class SumOfMultiples:

    def __init__(self, *nums: int) -> None:

        self.nums = set(nums) if nums else (3,5)

    def _return_sum_of_nums(self, ending_number: int) -> int:
        
        return sum(i for i in range(1, ending_number) 
                       if any(i % num == 0 for num in self.nums))
    
    @classmethod
    def sum_up_to(cls, final_number: int) -> int:

        return cls().to(final_number)
    
    def to(self, final_number: int) -> int:

        return self._return_sum_of_nums(final_number)