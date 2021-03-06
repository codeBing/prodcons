from threading import Thread
from time import ctime

class MyThread(Thread):

    def __init__(self, func, args, name=''):
        Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print 'starting', self.name, 'at:', ctime()
        self.res = apply(self.func,self.args)
        print self.name, 'finished at', ctime()

