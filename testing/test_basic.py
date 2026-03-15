from basicmath import div, sortlist, openfile

# def test_div():
#     assert div(4, 2) == 2

# def test_div_by_2():
#     assert div(15, 3) == 5

# def test_div_for_float():
#     assert div(1, 2) == 0.5


# def test_srt():
#     l = [5, 2, 9, 1, 5, 6]
#     sorted_l = [1, 2, 5, 5, 6, 9]
                
#     assert sortlist(l) == sorted_l



def test_open():
    filename = "missing_file.txt"

    try:
        openfile(filename)
        raise AssertionError("Expected exception not thrown")

    except FileNotFoundError:
        pass