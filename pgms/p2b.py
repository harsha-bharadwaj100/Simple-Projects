class NonVowelCounter:
    def __init__(self) -> None:
        self.var = ""

    def setString(self, st):
        self.var = st

    def countNonVowels(self):
        v = 0
        for i in self.var:
            if i.lower() in "aeiou":
                v += 1
        return len(self.var) - v


ctr = NonVowelCounter()
ctr.setString("qwertyuiop[asdfghjklzxcvbnm,1234567]")
print(ctr.countNonVowels())
