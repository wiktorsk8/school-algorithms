class Numbers:
    @staticmethod
    def generate():
        arr = []
        with open('test_numbers.txt') as file:
            lines = file.readlines()
            for line in lines:
                arr.append(int(line.strip()))
        return arr