class PerfectNumber:

    @classmethod
    def classify(cls, number):
        if number <= 0:
            raise ValueError("Input must be a positive integer")
        
        total = sum(cls._get_divisors(number))

        if total > number:
            return 'abundant'
        if total < number:
            return 'deficient'
        return 'perfect'
    
    @staticmethod
    def _get_divisors(number):
        return (num for num in range(1, number // 2 + 1) if number % num == 0)