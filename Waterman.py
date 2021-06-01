from tabulate import tabulate

def waterman(a, b, match, mismatch, gap):
    score = 0
    dot_arr = [[' '] * (len(a) + 2) for i in range(len(b) + 2)]
    dot_arr[0][1] = 'i'
    dot_arr[1][0] = 'j'
    dot_arr[1][1] = 0

    def p(alligns):
        cnt = 1
        for i in alligns:   
            print(f'\n({cnt})\n')
            count = 0
            for j in i:
                if count == 2: 
                    print(f'Score: {j}')
                else:
                    print(j)
                count += 1
            cnt += 1

    def traceback(seq1, seq2, dot_arr, col, row):
        allign = []
        if dot_arr[row][col] == 0: 
            return [["", "", 0]]

        if seq1[col-2] == seq2[row-2]:
            vals = traceback(seq1, seq2, dot_arr, col - 1, row - 1)
            for value in vals:
                value[0] += seq1[col-2]
                value[1] += seq1[col-2]
                value[2] += match
            allign += vals
        else:
            up = dot_arr[row - 1][col] 
            left = dot_arr[row][col - 1]
            diagonal = dot_arr[row - 1][col - 1]
            maxi = max(up,left,diagonal)
            if maxi == up:
                vals = traceback(seq1, seq2, dot_arr, col, row - 1)
                for value in vals:
                    value[0] += '-'
                    value[1] += seq2[row - 2]
                    value[2] += gap
                allign += vals
            if maxi == left:
                vals = traceback(seq1, seq2, dot_arr, col - 1, row)
                for value in vals:
                    value[0] += seq1[col - 2]
                    value[1] += '-'
                    value[2] += gap
                allign += vals
            if maxi == diagonal: 
                vals = traceback(seq1, seq2, dot_arr, col - 1, row - 1)
                for value in vals:
                    value[0] += seq1[col - 2]
                    value[1] += seq2[row - 2]
                    value[2] += mismatch
                allign += vals
        return allign


    for i in range(2, len(a) + 2):
        dot_arr[0][i] = a[i-2]
        dot_arr[1][i] = 0

    for i in range(2, len(b) + 2):
        dot_arr[i][0] = b[i-2]
        dot_arr[i][1] = 0

    max_value = 0
    mx = 0
    my = 0

    for i in range(2, len(a) + 2):
        for j in range(2, len(b) + 2):
            up = dot_arr[j-1][i] + gap
            left = dot_arr[j][i-1] + gap
            if dot_arr[j][0] == dot_arr[0][i]:
                diagonal = dot_arr[j-1][i-1] + match
            else:
                diagonal = dot_arr[j-1][i-1] + mismatch
            dot_arr[j][i] = max(up, left, diagonal, 0)
            if max_value <= dot_arr[j][i]:
                max_value = dot_arr[j][i]
                mx = j
                my = i

    print(tabulate(dot_arr, tablefmt="github"))
    final = traceback(a, b, dot_arr, my, mx)
    p(final)

#Main testcase
if __name__ == "__main__":  
    waterman(a = "ACGTTGACCTGTAACCTC" , b = "ACCTTGTCCTCTTTGCCC", match = 2, mismatch=-1, gap = -1) 

#|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|
#|   | i | A | C | G | T | T | G | A | C  | C  | T  | G  | T  | A  | A  | C  | C  | T  | C  |
#| j | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
#| A | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 1  | 0  | 0  | 0  | 0  | 2  | 2  | 1  | 0  | 0  | 0  |
#| C | 0 | 1 | 4 | 3 | 2 | 1 | 0 | 1 | 4  | 3  | 2  | 1  | 0  | 1  | 1  | 4  | 3  | 2  | 2  |
#| C | 0 | 0 | 3 | 3 | 2 | 1 | 0 | 0 | 3  | 6  | 5  | 4  | 3  | 2  | 1  | 3  | 6  | 5  | 4  |
#| T | 0 | 0 | 2 | 2 | 5 | 4 | 3 | 2 | 2  | 5  | 8  | 7  | 6  | 5  | 4  | 3  | 5  | 8  | 7  |
#| T | 0 | 0 | 1 | 1 | 4 | 7 | 6 | 5 | 4  | 4  | 7  | 7  | 9  | 8  | 7  | 6  | 5  | 7  | 7  |
#| G | 0 | 0 | 0 | 3 | 3 | 6 | 9 | 8 | 7  | 6  | 6  | 9  | 8  | 8  | 7  | 6  | 5  | 6  | 6  |
#| T | 0 | 0 | 0 | 2 | 5 | 5 | 8 | 8 | 7  | 6  | 8  | 8  | 11 | 10 | 9  | 8  | 7  | 7  | 6  |
#| C | 0 | 0 | 2 | 1 | 4 | 4 | 7 | 7 | 10 | 9  | 8  | 7  | 10 | 10 | 9  | 11 | 10 | 9  | 9  |
#| C | 0 | 0 | 2 | 1 | 3 | 3 | 6 | 6 | 9  | 12 | 11 | 10 | 9  | 9  | 9  | 11 | 13 | 12 | 11 |
#| T | 0 | 0 | 1 | 1 | 3 | 5 | 5 | 5 | 8  | 11 | 14 | 13 | 12 | 11 | 10 | 10 | 12 | 15 | 14 |
#| C | 0 | 0 | 2 | 1 | 2 | 4 | 4 | 4 | 7  | 10 | 13 | 13 | 12 | 11 | 10 | 12 | 12 | 14 | 17 |
#| T | 0 | 0 | 1 | 1 | 3 | 4 | 3 | 3 | 6  | 9  | 12 | 12 | 15 | 14 | 13 | 12 | 11 | 14 | 16 |
#| T | 0 | 0 | 0 | 0 | 3 | 5 | 4 | 3 | 5  | 8  | 11 | 11 | 14 | 14 | 13 | 12 | 11 | 13 | 15 |
#| T | 0 | 0 | 0 | 0 | 2 | 5 | 4 | 3 | 4  | 7  | 10 | 10 | 13 | 13 | 13 | 12 | 11 | 13 | 14 |
#| G | 0 | 0 | 0 | 2 | 1 | 4 | 7 | 6 | 5  | 6  | 9  | 12 | 12 | 12 | 12 | 12 | 11 | 12 | 13 |
#| C | 0 | 0 | 2 | 1 | 1 | 3 | 6 | 6 | 8  | 7  | 8  | 11 | 11 | 11 | 11 | 14 | 14 | 13 | 14 |
#| C | 0 | 0 | 2 | 1 | 0 | 2 | 5 | 5 | 8  | 10 | 9  | 10 | 10 | 10 | 10 | 13 | 16 | 15 | 15 |
#| C | 0 | 0 | 2 | 1 | 0 | 1 | 4 | 4 | 7  | 10 | 9  | 9  | 9  | 9  | 9  | 12 | 15 | 15 | 17 |
#
#(1)
#
#ACGTTGACCTGTAA-CCTC
#ACCTTGTCCTCTTTGCC-C
#Score: 17
#
#(2)
#
#ACGTTGACCTGTA-ACCTC
#ACCTTGTCCTCTTTGCC-C
#Score: 17
#
#(3)
#
#ACGTTGACCTG-TAACCTC
#ACCTTGTCCTCTTTGCC-C
#Score: 17
#
#(4)
#
#ACGTTGACCT-GTAACCTC
#ACCTTGTCCTCTTTGCC-C
#Score: 17