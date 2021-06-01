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

waterman(a = "ACGTTGACCTGTAACCTC" , b = "ACCTTGTCCTCTTTGCCC", match = 2, mismatch=-1, gap = -1)