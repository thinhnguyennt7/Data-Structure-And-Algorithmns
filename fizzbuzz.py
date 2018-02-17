# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
#  For numbers which are multiples of both three and five output “FizzBuzz”.


# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

def fizzBuzz(self, n):
        # """
        # :type n: int
        # :rtype: List[str]
        # """
        arr = []
        for i in range(n):
            i = i + 1
            if (i % 15 == 0):
                arr.append("FizzBuzz")
            elif (i % 5 == 0):
                arr.append("Buzz")
            elif (i % 3 == 0):
                arr.append("Fizz")
            else:
                arr.append(str(i))

        return arr
