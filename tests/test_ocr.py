import bank_ocr
import pytest

def test_check():
    assert 2==2

def test_ocr_account_number_123456789():
    test_string = ("" +
"    _  _     _  _  _  _  _ \n" +
"  | _| _||_||_ |_   ||_||_|\n" +
"  ||_  _|  | _||_|  ||_| _|\n" +
"                           ")

    test_account = "123456789"
    assert test_account == bank_ocr.ocr_account_number(test_string)

def test_ocr_account_number_234567891():
    test_string = ("" +
" _  _     _  _  _  _  _    \n" +
" _| _||_||_ |_   ||_||_|  |\n" +
"|_  _|  | _||_|  ||_| _|  |\n" +
"                           ")

    test_account = "234567891"
    assert test_account == bank_ocr.ocr_account_number(test_string)

def test_ocr_account_number_345678912():
    test_string = ("" +
" _     _  _  _  _  _     _ \n" +
" _||_||_ |_   ||_||_|  | _|\n" +
" _|  | _||_|  ||_| _|  ||_ \n" +
"                           ")

    test_account = "345678912"
    assert test_account == bank_ocr.ocr_account_number(test_string)

def test_ocr_account_number_346578912():
    test_string = ("" +
" _     _  _ _  _  _     _ \n" +
" _||_||_ |_  ||_||_|  | _|\n" +
" _|  ||_| _| ||_| _|  ||_ \n" +
"                           ")

    test_account = "346578912"
    assert test_account == bank_ocr.ocr_account_number(test_string)

def test_ocr_account_to_digit_1():
    test_string = ("" +
"    _  _     _  _  _  _  _ \n" +
"  | _| _||_||_ |_   ||_||_|\n" +
"  ||_  _|  | _||_|  ||_| _|\n" +
"                           ")
    first_digit = ("" +
    "   \n" +
    "  |\n" +
    "  |\n" +
    "   ")

    expected_result = [ ("" +
"   \n" +
"  |\n" +
"  |\n" +
"   "),("" +
" _ \n" +
" _|\n" +
"|_ \n" +
"   "),("" +
" _ \n" +
" _|\n" +
" _|\n" +
"   "),("" +
"   \n" +
"|_|\n" +
"  |\n" +
"   "),("" +
" _ \n" +
"|_ \n" +
" _|\n" +
"   "),("" +
" _ \n" +
"|_ \n" +
"|_|\n" +
"   "),("" +
" _ \n" +
"  |\n" +
"  |\n" +
"   "),("" +
" _ \n" +
"|_|\n" +
"|_|\n" +
"   "),("" +
" _ \n" +
"|_|\n" +
" _|\n" +
"   ")
]

    assert  bank_ocr.split_raw_line_to_raw_digits(test_string) == expected_result

def test_ocr_digit_1():
    test_string = ("" +
    "   \n" +
    "  |\n" +
    "  |\n" +
    "   ")
    assert "1" == bank_ocr.ocr_digit(test_string)

def test_ocr_digit_2():
    test_string = ("" +
    " _ \n" +
    " _|\n" +
    "|_ \n" +
    "   ")
    assert "2" == bank_ocr.ocr_digit(test_string)

def test_ocr_digit_3():
    test_string = ("" +
    " _ \n" +
    " _|\n" +
    " _|\n" +
    "   ")
    assert "3" == bank_ocr.ocr_digit(test_string)

def test_ocr_digit_4():
    test_string = ("" +
    "   \n" +
    "|_|\n" +
    "  |\n" +
    "   ")
    assert "4" == bank_ocr.ocr_digit(test_string)

@pytest.mark.skip(reason="no way of currently testing this")
def test_ocr_digit_5():
    test_string = ("" +
    " _ \n" +
    "|_ \n" +
    " _|\n" +
    "   ")
    assert "5" == bank_ocr.ocr_digit(test_string)
