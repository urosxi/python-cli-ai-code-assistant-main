# from functions.get_files_info import get_files_info

# print("Result for current directory:")
# print(get_files_info("calculator", "."))
#
# print("Result for 'pkg' directory:")
# print(get_files_info("calculator", "pkg"))

# print("Result for '/bin' directory:")
# print(get_files_info("calculator", "/bin"))

# print("Result for '../' directory:")
# print(get_files_info("calculator", "../"))


# from functions.get_file_content import get_file_content

# # print("Results for 'lorem.txt':")
# # print(get_file_content("calculator", "lorem.txt"))

# print("Results for 'main.py':")
# print(get_file_content("calculator", "main.py"))

# print("Results for 'pkg/calculator.py':")
# print(get_file_content("calculator", "pkg/calculator.py"))

# print("Results for '/bin/cat':")
# print(get_file_content("calculator", "/bin/cat"))

# print("Results for 'pkg/does_not_exist.py':")
# print(get_file_content("calculator", "pkg/does_not_exist.py"))

# from functions.write_file import write_file

# print("Results for 'lorem.txt':")
# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

# print("Results for 'pkg/morelorem.txt':")
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

# print("Results for '/tmp/temp.txt':")
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

from functions.run_python_file import run_python_file

print("Results for 'main.py'")
print(run_python_file("calculator", "main.py"))

print("Results for 'main.py [3 + 5]'")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("Results for 'tests.py'")
print(run_python_file("calculator", "tests.py"))

print("Results for '../main.py'")
print(run_python_file("calculator", "../main.py"))

print("Results for 'nonexistent.py'")
print(run_python_file("calculator", "nonexistent.py"))

print("Results for 'lorem.txt'")
print(run_python_file("calculator", "lorem.txt"))
