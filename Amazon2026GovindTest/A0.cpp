void fizzBuzz(int n) {
    for (int i = 1; i <= n; i++) {
        // Check if divisible by BOTH 3 and 5 first
        if (i % 3 == 0 && i % 5 == 0) {
            printf("FizzBuzz\n");
        }
        // Check if divisible by 3 only
        else if (i % 3 == 0) {
            printf("Fizz\n");
        }
        // Check if divisible by 5 only
        else if (i % 5 == 0) {
            printf("Buzz\n");
        }
        // If not divisible by either, print the number
        else {
            printf("%d\n", i);
        }
    }
}
