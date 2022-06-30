def up_array(arr):
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None
    num = "".join([str(el) for el in arr])
    x = str(int(num) + 1)
    res = [int(ele) for ele in x]

    return res
