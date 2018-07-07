
import time


runs = 10000

# Largest palindrome product

def main():
    global min_value
    global max_value

    min_value = 100
    max_value = 999
    min_product = min_value * min_value
    max_product = max_value * max_value

    for x in range(max_product, min_product, -1):
        x = str(x)
        if x == x[::-1]:
            if check_three_digits_multiplier(int(x)):
                return x;

def check_three_digits_multiplier(palindrome):

    for x in range (max_value, min_value, -1):
        if(palindrome % x == 0):
            if palindrome // x >= min_value and palindrome // x <= max_value:
                return True

    return False



if __name__ == "__main__":
    answer = 0
    total_time = 0

    for run in range(0, runs):
        start_time = time.time()
        answer = main()
        run_time = time.time() - start_time
        total_time += run_time

    print("answer  --- {} ---".format(answer))
    print("runtime --- {:.4f} ms ---".format((total_time * 1000) / runs))

