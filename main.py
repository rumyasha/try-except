from Utils.my_dicts import *
from Utils.my_math import *
from Utils.my_strings import *
from Utils.my_lists import *

try:
    print(add_element(d={}, key=34, value="fsffffffff"))
except TypeError as e:
    print(f"Ошибка типа: {e}")
except Exception as e:
    print(f"Другая ошибка: {e}")

try:
    print(remove_element(d={34: "fsffffffff"}, key=34))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(merge_dicts(d1={34: "fsffffffff"}, d2={45: "gggggggggggg"}))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(find_by_key(d={34: "fsffffffff"}, key=34))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(get_all_keys(d={34: "fsffffffff"}))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(get_all_values(d={34: "fsffffffff"}))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(sort_list(["gymngwqwwerghdfsf"]))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(get_max(["ggnhgrewrgf"]))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(get_min(["gsfgegeges"]))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(clear_list(["gsgeg"]))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(sum_of_elements([1,2,3,4,5]))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(count_elements(["fgsag"]))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(add(1,2))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(subtract(10,2))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(multiply(5,2))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(power(2,3))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(moduls(10,3))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(floor_division(10,3))
except Exception as e:
    print(f"{e}")

try:
    print(reverse_string("Hello, World!"))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(to_lowercase("Hello, World!"))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(to_uppercase("Hello, World!"))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(capitalize_words("hello, world!"))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(remove_spaces("Hello, World!"))
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print(count_characters("Hello, World!"))
except Exception as e:
    print(f"Ошибка: {e}")
