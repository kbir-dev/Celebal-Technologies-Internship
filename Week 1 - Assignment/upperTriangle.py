# Print Upper Triangle

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

def printUT(num):
    for i in range(1,num+1):
        print((i-1)*" "+"*"*(num-i+1))
        print(end="")
        