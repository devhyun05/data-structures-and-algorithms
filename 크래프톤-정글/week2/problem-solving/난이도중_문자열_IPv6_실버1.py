ipv6 = input()

if "::" in ipv6:     
    ipv6_split = ipv6.split("::")

    left_split = ipv6_split[0].split(":")
    right_split = ipv6_split[1].split(":")

    left_split_len = len(left_split)
    right_split_len = len(right_split)

    for i in range(left_split_len):
        curr_str_len = len(left_split[i])
        if curr_str_len < 4:
            left_split[i] = "0" * (4-curr_str_len)  + left_split[i]
    
    for i in range(right_split_len):
        curr_str_len = len(right_split[i])
        if curr_str_len < 4:
            right_split[i] = "0" * (4-curr_str_len)  + right_split[i]
    
    missing_zero = 8 - (left_split_len + right_split_len)
    zero_list = []

    for i in range(missing_zero):
        zero_list.append("0000")
    res = left_split + zero_list + right_split
    print(":".join(res))
else:
    ipv6_split = ipv6.split(":")
    ipv6_len = len(ipv6_split)

    for i in range(ipv6_len):
        curr_str_len = len(ipv6_split[i])
        if curr_str_len < 4:
            ipv6_split[i] = "0" * (4-curr_str_len) + ipv6_split[i]
    
    print(":".join(ipv6_split))


