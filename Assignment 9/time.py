class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def sum(self, guest):
        result = Time(None, None, None)
        result.hour = self.hour + guest.hour
        result.minute = self.minute + guest.minute
        result.second = self.second + guest.second
        if result.second >= 60:
            result.minute += 1
            result.second -= 60
        if result.minute >= 60:
            result.hour += 1
            result.minute -= 60
        return result
    def sub(self, guest):
        result = Time(None, None, None)
        result.hour = self.hour - guest.hour
        result.minute = self.minute - guest.minute
        result.second = self.second - guest.second
        if result.second < 0:
            result.minute -= 1
            result.second += 60
        if result.minute < 0:
            result.hour -= 1
            result.minute += 60
        return result
    def show_time(self):
        print(self.hour,':',self.minute,':',self.second)

t1 = Time(5,30,40)
print('T1 = ', end='')
t1.show_time()
t2 = Time(2,30,50)
print('T2 = ', end='')
t2.show_time()
sum_t = t1.sum(t2)
print('Sum of times = ', end='')
sum_t.show_time()
sub_t = t1.sub(t2)
print('Sub of times = ', end='')
sub_t.show_time()
        
        