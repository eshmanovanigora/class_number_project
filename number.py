class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool
        """
        return self.value % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value % 2 == 0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        c = 0
        for i in range(1, self.value + 1):
            if self.value % i:
                c += 1
        return c < 2

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        list_divisors = []
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                list_divisors.append(i)
        return list_divisors

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return (len(str(self.value)))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        sum = 0
        temp = str(self.value)
        for i in range(len(temp)):
            sum += int(temp[i])
        return sum

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        t = 0
        temp = self.value
        l = len(str(self.value))
        for i in range(l):
            t *= 10
            t += temp % 10
            temp //= 10
        return t

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        pass

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        list_digits = []
        for i in str(self.value):
            list_digits.append(int(i))
        return list_digits

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        list_digits = []
        for i in str(self.value):
            list_digits.append(int(i))
        return max(list_digits)        

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        list_digits = []
        for i in str(self.value):
            list_digits.append(int(i))
        return min(list_digits)   

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        if len(str(self.value)) == 1:
            return self.value
        sum = 0
        for i in range(1, self.value + 1):
            if self.value % i:
                sum += i
        return sum // len(str(self.value))

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        l = len(str(self.value))
        if l > 1:
            val = sorted(str(self.value))
            if len(val) % 2 == 0:
                return int(val[l // 2])
            else:
                return (int(val[l // 2]) + int(val[l // 2 + 1])) // 2

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        list_digits = []
        for i in str(self.value):
            list_digits.append(int(i))
        return max(list_digits) - min(list_digits)   

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        temp = str(self.value)
        freq = []
        for i in temp:
            freq.append(temp.count(i))
        return list(set(freq))
    

# Create a new instance of Number
number = Number(3)
print('the number = ', number.get_number())
print('it is odd.', number.is_odd())
print('it is even.', number.is_even())
print('it is prime.', number.is_prime())
print('the average = ', number.get_average())
print('digits = ', number.get_digits())
print('divisors = ', number.get_divisors())
print('frequency = ', number.get_frequency())
print('length = ', number.get_length())
print('max = ', number.get_max())
print('min = ', number.get_min())
print('median = ', number.get_median())
print('numbers -> ', number.get_number())
print('range = ', number.get_range())
print('reversed = ', number.get_reverse())
print('sum = ', number.get_sum())
