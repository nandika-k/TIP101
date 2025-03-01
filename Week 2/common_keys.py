def common_keys(dict1, dict2):
	common_keys = []
	for key in dict1:
		if key in dict2:
			common_keys.append(key)
	return common_keys

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)