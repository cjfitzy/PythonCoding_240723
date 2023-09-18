import random
red=0
red=0
green=0
yellow=0
class LotteryBall:
    def __init__(self, **balls):
        self.contents = {}
        for colour, count in balls.items():
            self.contents[colour] = count
     
    def pickaball(self):
        colour = random.choice(list(self.contents.keys()))

    #def check(self,ball):
    #    self.ball += amount
    #    return


hat = LotteryBall(red=5, blue=2, green=1,yellow=3)

pickaball = hat.pickavall
print(pickaball)














#so a hat with balls in it (Red = 5, Blue =2, Green = 1, Yellow=3 )
#hat = Hat(red=5, blue=2, green=1,yellow=3)
