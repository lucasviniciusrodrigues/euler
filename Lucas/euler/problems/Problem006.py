
import time

runs = 10000

# Sum square difference

def main():

    sum_squares = 0
    square_sum = 0

    for aux in range(1,101):
        sum_squares += aux * aux
        square_sum += aux

    square_sum *= square_sum

    return square_sum - sum_squares

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

