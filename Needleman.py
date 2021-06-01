from tabulate import tabulate


def needleman(a, b, match, mismatch, gap):
    dot_arr = [[' '] * (len(a) + 2) for i in range(len(b) + 2)]
    dot_arr[0][1] = 'i'
    dot_arr[1][0] = 'j'
    dot_arr[1][1] = 0

    for i in range(2, len(a) + 2):
        dot_arr[0][i] = a[i-2]
        dot_arr[1][i] = dot_arr[1][i-1] + gap

    for i in range(2, len(b) + 2):
        dot_arr[i][0] = b[i-2]
        dot_arr[i][1] = dot_arr[i-1][1] + gap

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

    #Traceback Function   
    def traceback(seq1, seq2, dot_arr, col, row):
        allign = []
        if col == 1 and row > 1:
            return [['-' * len(seq2[:row - 1]), seq2[:row - 1], gap]]
        if col > 1 and row == 1: 
            return [[seq1[:col - 1], '-' * len(seq1[:col - 1]), gap]]
        if col == 1 and row == 1: 
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
        for j in range(2, len(b) + 2):
            up = dot_arr[j-1][i] + gap
            left = dot_arr[j][i-1] + gap
            if dot_arr[j][0] == dot_arr[0][i]:
                diagonal = dot_arr[j-1][i-1] + match
            else:
                diagonal = dot_arr[j-1][i-1] + mismatch
            
            dot_arr[j][i] = max(up, left, diagonal)


    print(tabulate(dot_arr, tablefmt="github"))
    print("\nTraceback: ")
    #print(traceback(a, b, dot_arr, len(a) + 1, len(b) + 1))
    final = traceback(a, b, dot_arr, len(a) + 1, len(b) + 1)
    p(final)

if __name__ == "__main__":  
    needleman(a = "ACGTTGACCTGTAACCTC" , b = "ACCTTGTCCTCTTTGCCC", match = 2, mismatch=-1, gap = -1)

#|---|-----|-----|-----|----|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
#|   | i   | A   | C   | G  | T  | T  | G  | A  | C  | C  | T   | G   | T   | A   | A   | C   | C   | T   | C   |
#| j | 0   | -1  | -2  | -3 | -4 | -5 | -6 | -7 | -8 | -9 | -10 | -11 | -12 | -13 | -14 | -15 | -16 | -17 | -18 |
#| A | -1  | 2   | 1   | 0  | -1 | -2 | -3 | -4 | -5 | -6 | -7  | -8  | -9  | -10 | -11 | -12 | -13 | -14 | -15 |
#| C | -2  | 1   | 4   | 3  | 2  | 1  | 0  | -1 | -2 | -3 | -4  | -5  | -6  | -7  | -8  | -9  | -10 | -11 | -12 |
#| C | -3  | 0   | 3   | 3  | 2  | 1  | 0  | -1 | 1  | 0  | -1  | -2  | -3  | -4  | -5  | -6  | -7  | -8  | -9  |
#| T | -4  | -1  | 2   | 2  | 5  | 4  | 3  | 2  | 1  | 0  | 2   | 1   | 0   | -1  | -2  | -3  | -4  | -5  | -6  |
#| T | -5  | -2  | 1   | 1  | 4  | 7  | 6  | 5  | 4  | 3  | 2   | 1   | 3   | 2   | 1   | 0   | -1  | -2  | -3  |
#| G | -6  | -3  | 0   | 3  | 3  | 6  | 9  | 8  | 7  | 6  | 5   | 4   | 3   | 2   | 1   | 0   | -1  | -2  | -3  |
#| T | -7  | -4  | -1  | 2  | 5  | 5  | 8  | 8  | 7  | 6  | 8   | 7   | 6   | 5   | 4   | 3   | 2   | 1   | 0   |
#| C | -8  | -5  | -2  | 1  | 4  | 4  | 7  | 7  | 10 | 9  | 8   | 7   | 6   | 5   | 4   | 6   | 5   | 4   | 3   |
#| C | -9  | -6  | -3  | 0  | 3  | 3  | 6  | 6  | 9  | 12 | 11  | 10  | 9   | 8   | 7   | 6   | 8   | 7   | 6   |
#| T | -10 | -7  | -4  | -1 | 2  | 5  | 5  | 5  | 8  | 11 | 14  | 13  | 12  | 11  | 10  | 9   | 8   | 10  | 9   |
#| C | -11 | -8  | -5  | -2 | 1  | 4  | 4  | 4  | 7  | 10 | 13  | 13  | 12  | 11  | 10  | 12  | 11  | 10  | 12  |
#| T | -12 | -9  | -6  | -3 | 0  | 3  | 3  | 3  | 6  | 9  | 12  | 12  | 15  | 14  | 13  | 12  | 11  | 13  | 12  |
#| T | -13 | -10 | -7  | -4 | -1 | 2  | 2  | 2  | 5  | 8  | 11  | 11  | 14  | 14  | 13  | 12  | 11  | 13  | 12  |
#| T | -14 | -11 | -8  | -5 | -2 | 1  | 1  | 1  | 4  | 7  | 10  | 10  | 13  | 13  | 13  | 12  | 11  | 13  | 12  |
#| G | -15 | -12 | -9  | -6 | -3 | 0  | 3  | 2  | 3  | 6  | 9   | 12  | 12  | 12  | 12  | 12  | 11  | 12  | 12  |
#| C | -16 | -13 | -10 | -7 | -4 | -1 | 2  | 2  | 4  | 5  | 8   | 11  | 11  | 11  | 11  | 14  | 14  | 13  | 14  |
#| C | -17 | -14 | -11 | -8 | -5 | -2 | 1  | 1  | 4  | 6  | 7   | 10  | 10  | 10  | 10  | 13  | 16  | 15  | 15  |
#| C | -18 | -15 | -12 | -9 | -6 | -3 | 0  | 0  | 3  | 6  | 6   | 9   | 9   | 9   | 9   | 12  | 15  | 15  | 17  |
#
#Traceback: 
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

(4)

ACGTTGACCT-GTAACCTC
ACCTTGTCCTCTTTGCC-C
Score: 17

