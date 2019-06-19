from cky import CKY
from chart import CHART
import json

def main():
    with open("text.txt") as f:
        sentence = f.read().split()
        print("sentence : %s\n" %sentence)

    with open("rule.json", 'r') as f:
        json_dict = json.load(f)
        grammar = json_dict["gram"]
        dictionary = json_dict["dict"]
        print("grammar : %s \ndictionary : %s \n" % (grammar, dictionary))
    
    model1 = CKY(grammar, dictionary, sentence)
    cky_ans = model1.p()
    #model2 = CHART(grammar, dictionary, sentence)
    #model2.p()
    print("cky result : ")
    for i, a in enumerate(cky_ans):
        print("sentence[%s] : %s" % (i, a))

if __name__ == "__main__":
    main()