files_path = 'cs_data\\193_1.txt'
with open(files_path) as f:
    data = f.read()
    for i in ',.:?><"!\/;':
        data = data.replace(i, "")
    print(data)
