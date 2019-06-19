class CHART:
    def __init__(self, grammar_rule, dictionary_rule, sentence):
        """
        初期化する関数
        """
        self.s = sentence
        self.gram = grammar_rule
        self.dic = dictionary_rule
        self.l = len(self.s)
        self.agenda = []
        self.chart = []

    def init_agenda(self):
        cnt = 0
        for word in self.s:
            self.agenda.append([cnt + 1, cnt, cnt + 1, self.dic[word], [word, "."]])
            cnt += 1
        self.agenda.append([0, 0, list(self.gram.keys())[0], ["."].append(self.gram[list(self.gram.keys())[0]])])


    """
    def judge(self):
        if self.cnt.index('.') == len(self.cnt) -1 :
            self.act = -1
        else:
            self.act = 1 
        return self.act
    """

    def p(self):
        print("chart")
        self.init_agenda()
        print(self.agenda)