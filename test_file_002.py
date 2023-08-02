class Test_credence_001:

    def test_sum_003(self):
        a = 10
        b = 30
        mul = a*b
        print("mul of a and b:" + str(mul))
        if mul == 300:
            assert True
        else:
            assert False

    def test_sum_004(self):
        a = 40
        b = 30
        sub = a-b
        print("sub of a and b:" + str(sub))
        if sub == 10:
            assert True
        else:
            assert False