try: 
	f = open('test_file.txt')
	var = bad_var
	
excert FileNotFoundError as e:
	print(e)
excert Exception as e:
	print(e)
else:
	print(f.read())
	f.close()
finally
	print("Executing Finally...")