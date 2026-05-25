# Last updated: 5/25/2026, 1:35:01 PM
1class Solution:
2    def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
3        # e.g. if wordlist = ["xy", "ab", "xz"]
4        # then weights = [{x: 2, a: 1}, {b: 1, y:1, z:1}]
5        weights = [Counter(word[i] for word in wordlist) for i in range(6)]
6
7        # sort wordlist, least similar to rest of corpus first
8        wordlist.sort(key=lambda word: sum(weights[i][c] for i, c in enumerate(word)))
9
10        while wordlist:
11            # get the word most similar to the rest of the corpus by popping
12            # from the *end* of wordlist
13            word = wordlist.pop()
14            matches = master.guess(word)
15            # only those words that share exactly x characters with word can be
16            # the solution.
17            wordlist = [
18                other
19                for other in wordlist
20                if matches == sum(w == o for w, o in zip(word, other))
21            ]