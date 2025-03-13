# write functions here, don't add input('') statements here!

def get_bonus_pay_amount(sales):
    if sales < 0 or sales > 1999:
        return "Invalid arguments"
    elif sales <= 499:
        return sales * 0.05
    elif sales <= 999:
        return sales * 0.06
    elif sales <= 1499:
        return sales * 0.07
    elif sales <= 1999:
        return sales * 0.08

def test_get_bonus_pay_amount():
    assert get_bonus_pay_amount(-1) == "Invalid arguments"
    assert get_bonus_pay_amount(200) == 10
    assert get_bonus_pay_amount(600) == 36
    assert get_bonus_pay_amount(1000) == 70
    assert get_bonus_pay_amount(1500) == 120
    assert get_bonus_pay_amount(2000) == "Invalid arguments"

test_get_bonus_pay_amount()
