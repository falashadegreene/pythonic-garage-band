class Band:
   
    def __init__(self, name="none", members=[]):
        self.name = name
        self.members = members
        Band.all_bands.append(self)