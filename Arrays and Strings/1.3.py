# URLify



# My solution

def urlify1(string):
    # Run time O(n+m),  n is the length of the string, m is the number of spaces. Space O(1+m)
    # Average case O(n) time complexity
    return string.replace(" ", "%20")


# Book Solution 1

# Helper function to replace spaces with %20

def countSpaces(string):
    # Run time O(n), Space O(1)
    spaces = 0
    for char in string:
        if char == " ":
            spaces += 1
    return spaces

def urlify(string):
    # Run time O(n), Space O(1)
    spaces = countSpaces(string)
    index = len(string) + spaces * 2
    newString = [""] * index
    for char in string:
        if char == " ":
            newString[index - 1] = "0"
            newString[index - 2] = "2"
            newString[index - 3] = "%"
            index -= 3
        else:
            newString[index - 1] = char
            index -= 1
    return "".join(newString)


