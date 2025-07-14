def update_name():
    full_name = "Chuka Emeka"
    full_name = "Chuka Okeke"
    return full_name

print("1.", update_name())  # Output: Chuka Okeke


def bio_data(*, height, age):
    return f"I am {age} years old and my height is {height} meters."

print("2.", bio_data(height=1.75, age=23))  # Output: I am 23 years old and my height is 1.75 meters.


def check_login_status(is_logged_in=False):
    return type(is_logged_in)

print("3.", check_login_status(True))  # Output: <class 'bool'>


def full_name(first, last):
    return f"{first} {last}"

print("4.", full_name("Ada", "Obi"))  # Output: Ada Obi


def get_remainder(a, b):
    return a % b

print("5.", get_remainder(10, 3))  # Output: 1


def add_floats(a, b):
    return float(a) + float(b)

print("6.", add_floats(2.5, 3.5))  # Output: 6.0


def compare_numbers(a, b):
    return a >= b

print("7.", compare_numbers(5, 4))  # Output: True


def access_granted(has_id, has_clearance):
    return has_id and has_clearance

print("8.", access_granted(True, True))  # Output: True


def can_enter(has_pass, knows_manager):
    return has_pass or knows_manager

print("9.", can_enter(False, True))  # Output: True


def reverse_access(can_enter):
    return not can_enter

print("10.", reverse_access(True))  # Output: False


def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

print("11.", reverse_sentence("The boy is gone"))  # Output: gone is boy The


def get_odds(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))

print("12.", get_odds([1, 2, 3, 4, 5, 6]))  # Output: [1, 3, 5]


def total_word_count(*sentences):
    return sum(len(sentence.split()) for sentence in sentences)

print("13.", total_word_count("Hello world", "Python is fun"))  # Output: 5


from functools import reduce

def multiply(x, y):
    return x * y

def product_of_list(numbers):
    return reduce(multiply, numbers)

print("14.", product_of_list([1, 2, 3, 4]))  # Output: 24


def censor_vowels(word):
    vowels = "aeiouAEIOU"
    return ''.join('*' if char in vowels else char for char in word)

print("15.", censor_vowels("NaijaTech"))  # Output: N**j*T*ch
