def reverse_words(s):
    result = ""
    for word in s.split():
        for i in range(len(word) - 1, -1, -1):
            result += word[i]
            if i == 0:
                result += " "

    return result.strip()


if __name__ == '__main__':
    print(reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc")