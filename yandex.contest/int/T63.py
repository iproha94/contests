from collections import defaultdict


def hash_func(word):
    return "".join(sorted(word))


def f(words):
    groups = defaultdict(list)
    for word in words:
        groups[hash_func(word)].append(word)

    return groups.values()


a1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

r1 = [
  ["ate", "eat", "tea"],
  ["nat", "tan"],
  ["bat"]
]

print(f(a1))
