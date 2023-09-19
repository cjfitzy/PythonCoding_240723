import random
red=0
red=0
green=0
yellow=0
class LotteryBall:
    def __init__(self, **balls):
        self.contents = {}

        for color, count in balls.items():
            self.contents[color] = count
     
    def pickaball(self):
        color = random.choice(list(self.contents.keys()))
        return color


hat = LotteryBall(red=5, blue=2, green=1,yellow=3)

pickaball = hat.pickaball()
print(pickaball)


#so a hat with balls in it (Red = 5, Blue =2, Green = 1, Yellow=3 )
#hat = Hat(red=5, blue=2, green=1,yellow=3)
