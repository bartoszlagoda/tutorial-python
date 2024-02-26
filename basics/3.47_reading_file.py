print("===================")
print("       READ()      ")
print("===================")
# otwieranie pliku
file = open("../resources/message.txt")
# 1. odczytywanie zawartości ze zmiennej file
contents = file.read() # odczytuje pełny plik z odpowiednim formatowaniem
print(contents)
# zamykanie pliku
file.close()

print("===================")
print("    READLINES()    ")
print("===================")
file = open("../resources/message.txt")
# 2. odczytywanie zawartości ze zmiennej file
contents = file.readlines() # odczytuje pełny plik z zapisem jak w metodzie print()
print(contents)
file.close()

print("===================")
print("  FOR LINE IN FILE ")
print("===================")
file = open("../resources/message.txt")
# 3. odczytywanie zawartości ze zmiennej file
for line in file:
    print(line)
file.close()