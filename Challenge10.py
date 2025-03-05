# 📢 Day 10 – Daily Challenge "Anagram Checker"
print("\033[1;31mDay 10 Daily Python Challenge\033[0m")
print("✅\033[1;32;2m Anagram Checker ✅\n")

def are_anagrams(s1, s2):
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))

word1 = input("\033[1;31mEnter first word:\033[0m ")
word2 = input("\033[1;31mEnter second word:\033[0m ")
print("\n")
print("\033[1;31mYes! it's an anagram!.✅\033[0m\n" if are_anagrams(word1, word2) else "\033[1;31mNo! it's not an anagram!.❌\033[0m\n")
