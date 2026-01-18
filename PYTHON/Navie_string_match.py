def naive_string_match(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)

    for i in range(text_len - pattern_len + 1):
        if text[i:i + pattern_len] == pattern:
            print(f"Pattern found at index {i}")

# Testing Example
if __name__ == "__main__":
    print("MOHIT PRAJAPATI")
    print("FYCS")
    print("22549")
    text = "ababcabcabababd"
    pattern = "abab"
    naive_string_match(text, pattern)