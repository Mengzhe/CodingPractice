def textJustification(words, l):
    res = []
    cur_line = []
    cur_num_chars = 0
    for word in words:
        if len(cur_line) == 0:
            cur_line.append(word)
            cur_num_chars += len(word)
            # print(cur_line)
            continue
        if cur_num_chars + len(cur_line) + len(word) <= l:
            cur_line.append(word)
            cur_num_chars += len(word)
        else:
            # print(cur_line)
            num_words = len(cur_line)
            if num_words > 1:
                slots_spaces = num_words - 1
                quotient, remainder = divmod(l - cur_num_chars, slots_spaces)
                for i in range(remainder):
                    cur_line[i] = cur_line[i] + ' ' * (quotient + 1)
                for i in range(remainder, slots_spaces):
                    cur_line[i] = cur_line[i] + ' ' * quotient

                res.append(''.join(cur_line))
            else:
                res.append(cur_line[0] + ' ' * (l - cur_num_chars))

            cur_line = []
            cur_num_chars = 0
            cur_line.append(word)
            cur_num_chars += len(word)

    ## last line
    if len(cur_line) > 0:
        # print("cur_num_chars", cur_num_chars)
        num_words = len(cur_line)
        res.append(' '.join(cur_line) + ' ' * (l - cur_num_chars - num_words + 1))

    return res


