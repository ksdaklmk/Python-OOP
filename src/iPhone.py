class iPhone:

    iPhone_list = ['8s', 'X', 'XS', '11']

    def __init__(self, model):
        self.model = model
    
    @classmethod
    def from_year(cls, year):
        return cls(iPhone.iPhone_list[int(year) - 2010])
    
    @staticmethod
    def newest_model():
        return iPhone.iPhone_list[len(iPhone.iPhone_list) - 1]
    
    def __repr__(self):
        return self.model


if __name__ == "__main__":
    a = iPhone('X')
    b = iPhone.from_year(2008)

    print("Newest model: " + iPhone.newest_model())
    print("a has " + str(a))
    print("b has " + str(b))
    print("a == b: " + str(a == b))
    print("a.model == b.model: " + str(a.model == b.model))
    
