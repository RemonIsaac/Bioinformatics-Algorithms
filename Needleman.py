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

#Main testcase
needleman(a = "ACGTTGACCTGTAACCTC" , b = "ACCTTGTCCTCTTTGCCC", match = 2, mismatch=-1, gap = -1)

