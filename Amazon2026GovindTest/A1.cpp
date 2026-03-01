#include <stdio.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
    int x = *(int*)a, y = *(int*)b;
    return (x > y) - (x < y);
}

int* medians(int values_count, int* values, int k, int* result_count) {
    qsort(values, values_count, sizeof(int), cmp);
    
    int n = values_count;
    int median_idx = (k - 1) / 2;
    
    int* result = (int*)malloc(2 * sizeof(int));
    *result_count = 2;
    
    result[0] = values[(n - k) + median_idx];  // max median
    result[1] = values[median_idx];             // min median
    
    return result;
}

// Test runner
void test(int* vals, int n, int k, int exp_max, int exp_min) {
    int* v = malloc(n * sizeof(int));
    for(int i=0;i<n;i++) v[i]=vals[i];
    int rc;
    int* r = medians(n, v, k, &rc);
    printf("max=%d (exp %d) %s | min=%d (exp %d) %s\n",
        r[0], exp_max, r[0]==exp_max?"✓":"✗",
        r[1], exp_min, r[1]==exp_min?"✓":"✗");
    free(r); free(v);
}

int main() {
    // Sample 0: [56,21], k=1
    int t0[] = {56, 21};
    test(t0, 2, 1, 56, 21);
    
    // Example: [1,2,3], k=2
    int t1[] = {1, 2, 3};
    test(t1, 3, 2, 2, 1);
    
    // k=n (only one subseq)
    int t2[] = {3, 1, 4};
    test(t2, 3, 3, 3, 3);  // sorted [1,3,4], median_idx=1 → 3
    
    // k=1 (min=min_elem, max=max_elem)
    int t3[] = {5, 2, 8, 1};
    test(t3, 4, 1, 8, 1);
    
    // k=5, [3,1,4,1,5,9,2,6]
    int t4[] = {3,1,4,1,5,9,2,6};
    test(t4, 8, 5, 5, 2);
    
    // All same elements
    int t5[] = {7, 7, 7};
    test(t5, 3, 2, 7, 7);
    
    // Single element
    int t6[] = {42};
    test(t6, 1, 1, 42, 42);
    
    return 0;
}
