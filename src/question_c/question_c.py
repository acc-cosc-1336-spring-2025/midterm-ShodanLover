#write functions here, don't add input('') statements here!

def reverse_string(string1):
    reversed_string = ""
    index = len(string1) - 1
    while index >= 0:
        reversed_string += string1[index]
        index -= 1
    return reversed_string

def test_reverse_string():
    assert reverse_string("hello world") == "dlrow olleh", "Test case 1 failed"
    assert reverse_string("hello") == "olleh", "Test case 2 failed"

test_reverse_string()