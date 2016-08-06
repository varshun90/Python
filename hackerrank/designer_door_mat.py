N = int(input("Enter no.of rows:"))
M = int(input("Enter no.of coloums:"))

def main():

    # Print top row
    for i in range(0, int((N) / 2)):
        no_of_patterns = i + i + 1
        no_of_dashes = int((M - (no_of_patterns * 3)) / 2)
        print_string(no_of_dashes, "-")
        print_string(no_of_patterns, ".|.")
        print_string(no_of_dashes, "-")
        print("")

    # print welcome
    print("WELCOME".center(M, "-"))

    # print bottom row
    for i in range(int((N) / 2)+1, N):
        patterns = (2 * (N - i)) - 1
        dashes = int((M - (patterns * 3)) / 2)
        print_string(dashes, "-")
        print_string(patterns, ".|.")
        print_string(dashes, "-")
        print("")

def print_string(no_of_times, string_to_print):
    for j in range(0, no_of_times):
        print(string_to_print, end="")


main()
