class Food:

    def __init__(self, name, type, style):
        self.name = name
        self.type_list = ["seafood", "fish", "pork", "beef", "chicken", "duck", "quail", "lamb", "vegetarian", "venison"]
        self.style_list = ["fried", "stir-fried", "steamed", "boiled", "soup", "wrapped", "grilled", "caramelized", "salad", "stew", "bbq"]
        self.type = type
        self.style = style

    def __str__(self):
        return f"{self._name} served with {self._style} {self._type}"

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def style(self):
        return self._style

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Empty name.")
        self._name = name
    
    @type.setter
    def type(self, type):
        type = type.lower()
        if type not in self.type_list:
            raise ValueError("Invalid food type")
        self._type = type

    @style.setter
    def style(self, style):
        style = style.lower()
        if style not in self.style_list:
            raise ValueError("Invalid food cooking style")
        self._style = style