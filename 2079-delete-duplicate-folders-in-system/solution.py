class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = {}
        for p in paths:
            t = root
            for w in p:
                t = t.setdefault(w, {})
        cnt = {}

        def ser(t):
            s = "(" + ",".join(k+ser(t[k]) for k in sorted(t)) + ")" if t else ""
            if t:
                cnt[s] = cnt.get(s, 0) + 1
            t['#'] = s
            return s

        ser(root)
        res =[ ]

        def dfs(t, curr):
            for k, v in t.items():
                if k == '#':
                    continue
                if v and 1 < cnt.get(v['#'], 0):
                    continue
                res.append(curr + [k])
                dfs(v, curr + [k])

        dfs(root, [])
        return res
