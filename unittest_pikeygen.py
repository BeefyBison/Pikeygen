import unittest
import passgen

class TestCreate_Random_String(unittest.TestCase):
    def test_empty_password_or_and_empty_sack(self):
        assert passgen.create_random_string is not None

    def test_double_tap(self):
        self.assertTrue(passgen.calculate_salt("abc").endswith('lv1lv1'))
        self.assertTrue(passgen.calculate_salt("hello6").endswith('gp6gp6'))
        self.assertTrue(passgen.calculate_salt("bebop9").endswith('vq9vq9'))

    def test_remove_number(self):
        rn_test_1 = passgen.remove_number("system1-tests")
        self.assertFalse("1" in rn_test_1)

    def test_remove_special(self):
        rs_test_1 = passgen.remove_special("system!-tests")
        self.assertFalse("!" in rs_test_1)

    def test_put_back_number(self):
        pbn_test_1 = passgen.put_back_number("ad", "system1-tests")
        self.assertTrue("ad1" == pbn_test_1)

    def test_length_passwords(self):
        password = passgen.main("")
        if len(password) > 20 or len(password) < 16:
            self.assertFalse

    def test_repetitive_passwords(self):
        pass_list = []
        for _x in range(50):
            pass_list.append(passgen.main(""))
        pass_set = set(pass_list)
        if len(pass_list) == len(pass_set):
            self.assertTrue
        else:
            self.assertFalse

    def test_repetitive_characters(self):
        for _x in range(50):
            input_str = passgen.main("")
            for el in input_str:
                if el * 4 in input_str:
                    self.assertFalse
                else:
                    self.assertTrue

if __name__ == "__main__":
    unittest.main(verbosity=2)
