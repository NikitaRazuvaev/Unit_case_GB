class ListComparer:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
    
    def compare_lists(self):
        calculator1 = AverageCalculator(self.list1)
        average1 = calculator1.calculate_average()
        
        calculator2 = AverageCalculator(self.list2)
        average2 = calculator2.calculate_average()
        
        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        elif average1 < average2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"