class Solution:
    def findDuplicate(self, paths):
        dict = {}
        for path in paths:
            dir = path.split(" ")
            for i in range(1, len(dir)):
                content = dir[i].split("(")[1][:-1]

                if content in dict.keys():
                    dict[content].append(dir[0] + "/" + dir[i].split("(")[0])
                else:
                    dict[content] = [dir[0] + "/" + dir[i].split("(")[0]]
        ans = []
        for i in dict:
            if len(dict[i]) > 1:
                ans.append(dict[i])

        return ans
