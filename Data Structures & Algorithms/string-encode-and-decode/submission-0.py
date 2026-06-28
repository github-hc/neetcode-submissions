class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            print(s)
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            print(length)
            print(i,j)
            word = s[j + 1 : j + 1 + length]
            print(word)
            res.append(word)

            i = j + 1 + length

        return res

