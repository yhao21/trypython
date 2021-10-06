import time
"""
polymorphism的常用方法：

通过抽象类完成多态



案例：
你设计了一个很厉害的文本编辑器 document，
他可以对任何类型的文件进行编辑，如word，pdf，excel

当你使用document打开某一个文件之前，你是不知道这个文件具体是哪一个类型的文件的
但是文件打开过程中程序识别到了这个文件是pdf或者word，他就会自动调用word编辑器的方法去打开word，pdf也同理。
这就要求，你在写document程序的时候，对每一种文件类型都要书写一个类，类下面都有一个编辑的方法（函数）
这样，你在通过document打开编辑某一个类型的文件时，实际上是执行了   word.编辑()  或者 pdf.编辑()的方法。



"""
class Document:
    def __init__(self,name):
        self.name = name

    def show(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Pdf(Document):
    def show(self):
        return 'show pdf contents'

class Word(Document):
    def show(self):
        return 'show word contents'


"""
raise NotImplementedError('Subclass must implement abstract method')

这个是手动报错，括号里是报错内容
这个报错是为了防止子类直接调用document的show方法，
目的在于，子类必须自己写自己的show方法

这个在下一章会详细讲述
"""

pdf_obj = Pdf('pdf file name.pdf')
word_obj = Word('word file name.docx')

print(pdf_obj.show())
"""return: show pdf contents"""

"""现在这样每次都通过对象名.show()并没有通过一个接口调用，那我们可以把它们放到一个列表里，然后用for循环达到通过o.show()这个端口统一调用"""

files = [pdf_obj,word_obj]
for o in files:
    print(o.show())
"""
returns:
    show pdf contents
    show word contents
"""






"""如果我不写子类的show，直接调用父类的show会怎么样呢？"""


class Document1:
    def __init__(self,name):
        self.name = name

    def show(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Pdf1(Document1):

    pass


class Word1(Document1):

    def show(self):
        return 'show word contents'

pdf_obj1 = Pdf1('file_name.pdf')
#pdf_obj1.show()
"""
return: NotImplementedError: Subclass must implement abstract method

这就是我们在父类中写的报错，子类不能执行父类的show，必须写自己的show
"""
