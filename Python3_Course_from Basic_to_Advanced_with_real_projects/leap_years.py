def is_test_data_leap(test_data):
    result_leap = []
    result_not = []
    for i in range(len(test_data)):
        if test_data[i] % 4 == 0 and test_data[i] % 100 != 0 or test_data[i] % 400 == 0:
            result_leap.append(test_data[i])
        else:
            result_not.append(test_data[i])

    return f'The test_datas {result_leap} are leap test_datas and the test_datas {result_not} are NOT leap test_datas!'


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

print(is_test_data_leap(test_data))
