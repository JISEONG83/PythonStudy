class myClass:
    pass # empty class

class Rectangle:
    count = 0  # 클래스 변수
 
    # 초기자(initializer)
    def __init__(self, width=1, height=1):
        # self.* : 인스턴스변수
        self.width = width
        self.height = height
        Rectangle.count += 1
        print('Called function(__init__)')

    def __call__(self, width, height):
        self.width = width
        self.height = height
        print('Called function(__call__)')

    def __add__(self, other):
        obj = Rectangle(self.width + other.width, self.height + other.height)
        return obj

    def __sub__(self, other):
        obj = Rectangle(self.width - other.width, self.height - other.height)
        return obj
 
    # 메서드
    def calcArea(self):
        area = self.width * self.height
        return area

    # 정적 메서드
    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight   
 
    # 클래스 메서드
    @classmethod
    def printCount(cls):
        print(cls.count)   



# 객체 생성
r = Rectangle()# __init__
r(2,5) # __call__
 
# 메서드 호출
area = r.calcArea()
print("area = ", area)
 
# 인스턴스 변수 엑세스
r.width = 10
print("width = ", r.width)
 
# 클래스 변수 엑세스
print(Rectangle.count)
print(r.count)

square = Rectangle.isSquare(5, 5)        
print(square)   # True        
 
rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)
rect1.printCount()  # 2 

print(Rectangle.count) #3

rect1+rect2
rect1-rect2
print("width = ", rect1.width)
print(Rectangle.count)