# lab.py

class BMI:
    def __init__(self, weight, height):
        # weight in kilograms
        # height in meters
        self.Weight = weight
        self.Height = height

    def BMI_Value(self):
        """
        Calculates BMI using the formula:
        Weight / (Height^2)
        """
        return self.Weight / (self.Height ** 2)

    def __eq__(self, other):
        """
        Overrides the equals method to compare
        weight and height of two BMI objects.
        """
        if not isinstance(other, BMI):
            return False
        return self.Weight == other.Weight and self.Height == other.Height


# --------- Testing the class ----------
if __name__ == "__main__":
    person1 = BMI(70, 1.75)
    person2 = BMI(70, 1.75)

    print("Person 1 BMI:", person1.BMI_Value())
    print("Person 2 BMI:", person2.BMI_Value())
    print("Are both persons equal?", person1 == person2)
