import itertools

class CKY:
    def __init__(self, grammar_rule, dictionary_rule, sentence):
        """
        初期化する関数
        """
        self.s = sentence
        self.gram = grammar_rule
        self.dic = dictionary_rule
        self.l = len(self.s)
        self.dic_cnt = { i:0 for i in set(self.dic.values())}
        self.gram_cnt = { i:0 for i in set(self.gram.keys())}
        self.table = {}

    def init_array(self):
        """
        データテーブルの初期化を行う関数
        """
        self.cky_array = [[i] for i in self.s]
        for i, word in enumerate(self.s):
            x = self.dic[word]
            self.dic_cnt[x] += 1
            self.table[x + str(self.dic_cnt[x])] = [self.cky_array[i][0]]
            self.cky_array[i].append([x + str(self.dic_cnt[x])])
        print(self.cky_array)

    def parse(self):
        """
        解析する関数
        """
        for i in range(2, self.l + 1):
            print("%s行目" % i)
            for j in range(self.l - i + 1):
                print("%s列目" % j)
                val = []
                for k in range(i - 1):
                    print((j, k + 1),(j + k + 1, i - k - 1))
                    for key, elem in self.gram.items():
                        for pair in elem:
                            for v1, v2 in itertools.product(self.cky_array[j][k + 1], self.cky_array[j + k + 1][i - k - 1]):
                                if [v1[:-1], v2[:-1]] in [pair]:
                                    self.gram_cnt[key] += 1
                                    ch = key + str(self.gram_cnt[key])
                                    self.table[ch] = [v1, v2]
                                    val.append(ch)
                if val:
                    self.cky_array[j].append(val)
                else:
                    self.cky_array[j].append(["_"])
                print(self.gram_cnt)
                print("")
            print(self.cky_array)
            print("")

    def out(self, array):
        """
        tableからS式を生成するための関数
        """
        stack = []
        for ans in array:
            if ans in self.table:
                x = self.out(self.table[ans])
                stack.append(x)
            else:
                return ans
        return stack

    def p(self):
        """
        処理を管理する関数
        """
        print("cky")
        self.init_array()
        self.parse()
        print("data table = %s\n" % self.cky_array)
        print("dictionary = %s\n" % self.table)
        result = self.out(self.cky_array[0][self.l])
        return result
        