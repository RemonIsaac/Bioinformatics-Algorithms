from tabulate import tabulate

def dot_matrix(seq1, seq2, size, step, thresh):
    dot_arr = [[' ']* (len(seq1)+1) for i in range(len(seq2) + 1)] 
    for i in range(1, len(seq1) + 1):
        dot_arr[0][i] = seq1[i-1]

    for i in range(1, len(seq2) + 1):
        dot_arr[i][0] = seq2[i-1]

    def thresh_check(a, b): 
        count = 0
        for j,i in zip(a,b):
            if i == j:
                count += 1
        if count >= thresh: 
            return True

    for i in range(0, len(seq1) - size + 1, step):
        for j in range(0, len(seq2) - size + 1, step):
            if thresh_check(seq1[i: i + size], seq2[j: j + size]): 
                dot_arr[j + size//2 + 1][i + size//2 + 1] = 'x'

    print(tabulate(dot_arr, tablefmt="github"))   
 
if __name__ == "__main__":
    dot_matrix(seq1 = "ACCTTGTCCTCTTTGCCC" , seq2 = "ACGTTGACCTGTAACCTC", size = 9, step=3, thresh = 4)

