def romanToInt(s: str) -> int:
    roman_to_value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_exceptions = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}

    total = 0
    prev = None
    for idx in range(0, len(s)):
        curr = s[idx]
        total += roman_to_value_map.get(curr)

        if prev in roman_exceptions.keys():
            if curr in roman_exceptions.get(prev):
                total -= roman_to_value_map.get(prev) * 2

        prev = curr

    return total


print(romanToInt("III") == 3)
print(romanToInt("IV") == 4)
print(romanToInt("IX") == 9)
print(romanToInt("LVIII") == 58)
print(romanToInt("MCMXCIV") == 1994)
print(romanToInt("DCXXI") == 621)
