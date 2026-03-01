def merge_sort(lst):
    if len(lst) == 0:
        return
    elif len(lst) == 1:
        return
    else:
        mid = len(lst) // 2
        left_lst = lst[ : mid]
        right_lst = lst[mid : ]
        
        print(f"\nSPLITTING {lst} INTO:\n -> left_side: {left_lst}\n -> right_side: {right_lst}")
        
        merge_sort(left_lst)
        merge_sort(right_lst)
        
        merged = merge(left_lst, right_lst)
        
        for i in range(len(merged)):
            lst[i] = merged[i]


def merge(srt_lst1, srt_lst2):
    print(f"\nMERGING {srt_lst1} AND {srt_lst2}...")
    merged_list = []
    idx_1 = 0
    idx_2 = 0
    
    while idx_1 < len(srt_lst1) and idx_2 < len(srt_lst2):
        if srt_lst1[idx_1] < srt_lst2[idx_2]:
            print(f" - Adding left_side[{idx_1}] -> {srt_lst1[idx_1]}")
            merged_list.append(srt_lst1[idx_1])
            idx_1 += 1
        else:
            print(f" - Adding right_side[{idx_2}] -> {srt_lst2[idx_2]}")
            merged_list.append(srt_lst2[idx_2])
            idx_2 += 1            
            
    while idx_1 < len(srt_lst1):
        print(f" - Adding left_side[{idx_1}] -> {srt_lst1[idx_1]}")
        merged_list.append(srt_lst1[idx_1])
        idx_1 += 1
        
    while idx_2 < len(srt_lst2):
        print(f" - Adding right_side[{idx_2}] -> {srt_lst2[idx_2]}")
        merged_list.append(srt_lst2[idx_2])
        idx_2 += 1
        
    print(f"Merged list: {merged_list}")
    return merged_list


if __name__ == "__main__":
    lst = [5, 8, 6, 1, 9, 3, 0, 2]
    merge_sort(lst)
    print(lst)
