class Tank:
    

    # 초기화
    def __init__(self):
        print '탱크가 생성되었습니다.'
        self.bal = 5
        self.x = 0
        self.y = 0
    
    def shoot(self):
        if self.bal == 0:
            print '포탄이 부족합니다.'
        else:
            self.bal -= 1
    
    def reload(self):
        self.bal = 5
        print '포탄을 장전했습니다. (남은 포탄 : ' , self.bal , ')'

    def move_x(self):
        self.x += 1
        self.position()
    
    def move_y(self):
        self.y += 1
        self.position()
    
    def position(self):
        print '탱크가 이동하였습니다. (현재 좌표 : (', self.x , ',', self.y, '))'



    # 포탄수 출력
    def cannon(self):
        print self.bal
