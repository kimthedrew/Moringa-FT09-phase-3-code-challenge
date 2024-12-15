class Magazine:
    def __init__(self, id, name, category="Uncategorized"): 
        self.id = id
        self.name = name
        self.category = category 
  
    @property
    def category(self):
        return self._category

    # Setter for category
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value  # Valid value is assigned

    def __repr__(self):
        return f"<Magazine id={self.id}, name={self.name}, category={self.category}>"
