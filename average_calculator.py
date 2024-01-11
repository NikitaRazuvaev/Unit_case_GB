class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def calculate_average(self):
        if len(self.numbers) == 0:
            return 0
        return sum(self.numbers) / len(self.numbers)