from atcoderbase import AtCoderBase


class ABC142A(AtCoderBase):
    def process(self):
        n = int(self.input())
        if n == 1:
            self.print(1)
            return
        if n % 2 == 0:
            self.print(0.5)
        else:
            self.print((n // 2 + 1) / n)
