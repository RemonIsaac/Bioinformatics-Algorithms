from tabulate import tabulate

def dot_matrix(a, b, size, step, thresh):
    dot_arr = [[' ']* (len(a)+1) for i in range(len(b) + 1)] 
    for i in range(1, len(a) + 1):
        dot_arr[0][i] = a[i-1]

    for i in range(1, len(b) + 1):
        dot_arr[i][0] = b[i-1]

    def thresh_check(a, b): 
        count = 0
        for i,j in zip(a,b):
            if i == j:
                count += 1
        if count >= thresh: 
            return True

    for i in range(0, len(b) - size + 1, step):
        for j in range(0, len(a) - size + 1, step):
            if thresh_check(a[i*step: i*step + size], b[j*step: j*step + size]): 
                dot_arr[j*step + size//2 + 1][i*step + size//2 + 1] = 'x'

    print(tabulate(dot_arr, tablefmt="github"))    



