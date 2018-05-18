with open('./4/test_cdhit.fa', 'w') as f:
    with open('./4/test.fa') as f1:
        seq = ''
        label = 0
        for line in f1:
            if '>' in line:
                if seq:
                    f.write(seq + '\n')
                seq = ''
                f.write(line)
            else:
                seq += line.strip()
        f.write(seq + '\n')
