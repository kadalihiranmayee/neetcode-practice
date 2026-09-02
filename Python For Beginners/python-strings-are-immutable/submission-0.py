def remove_fourth_character(word: str) -> str:
    if len(word)>4:
        before_fourth = word[:3] # "I"
        after_fourth = word[4:]  # "will never change."
        new_message = before_fourth + after_fourth
        return new_message


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
