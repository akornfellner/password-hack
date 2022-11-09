class Password:
    def __init__(self, input: str):
        self.pw = []

        for i in input:
            self.pw.append(ord(i)-97)

    def next(self):
        index = len(self.pw)-1
        finished = False

        while index >= 0 and not finished:
            self.pw[index] = next_value(self.pw[index])
            if self.pw[index] == 0:
                index -= 1
            else:
                finished = True

    def encode(self):
        return str(self).encode("ascii")

    def __str__(self):
        result = ""

        for i in self.pw:
            result += chr(i+97)

        return result


def next_value(x: int):
    if x == 7 or x == 10 or x == 13:
        return x+2
    return (x+1) % 26
