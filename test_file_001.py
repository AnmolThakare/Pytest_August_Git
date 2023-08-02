from selenium import webdriver

class Test_credence:

    def test_sum_001(self):
        a = 10
        b = 30
        sum = a+b
        print("sum of a and b:" + str(sum))
        if sum == 40:
            assert True
        else:
            assert False

    def test_sum_002(self):
        a = 10
        b = 30
        sum = a+b
        print("sum of a and b:" + str(sum))
        if sum == 40:
            assert True
        else:
            assert False


    def test_CredenceUrl_002(self):
        driver = webdriver.Firefox()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("you are at credence.in")
            assert True
        else:
            print("you are at wrong url")
            assert False
