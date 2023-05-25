# Int: frequency
# Int: value
# Bool: masking
class tonePoint:
    def __init__(self, frequency, value, masking):
        self.frequency = frequency
        self.masking = masking
        self.value = value

    def __str__(self):
        return f"frequency: {self.frequency}, value: {self.value}, masking: {self.masking}"