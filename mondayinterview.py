# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values. 
# For example, given the following object/dictionary as input:
# ```
example = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
# ```
# Your algorithm should return 41, the sum of the values 23 and 18. 
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process. 

def add_nums(obj):
    # print(obj)
    count = 0
    for v in obj.values():
        # check to see if values are a number
        # print(obj[key] == int)
        if type(v) == int:
            count += v
    return count

print(add_nums(example))