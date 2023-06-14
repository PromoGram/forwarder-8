with open("words.txt", "r", encoding="utf-8") as f:
    words = f.read().splitlines()
f.close()
with open ("words.txt", "w", encoding="utf-8") as f:
    f.write(str(words))
f.close()


# with open("groups.txt", "r", encoding="utf-8") as f:
#     groups = f.read().splitlines()
# f.close()
# new = []
# for group in groups:
#     if "+" in group:
#         new.append(group)
#     else:
#         new.append(group.split("https://t.me/")[1])
# with open ("groups.txt", "w") as f:
#     f.write(str(new))