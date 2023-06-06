class person:
    def __init__(self, name="", height_in_cm=0, weight_in_kg=0):
        self.name = name
        self.height_in_cm = height_in_cm
        self.weight_in_kg = weight_in_kg

    def get_weight(self, metric:str="kg"):
        if metric == "kg":
            return self.weight_in_kg
        elif metric == "g":
            return self.weight_in_kg*1000

