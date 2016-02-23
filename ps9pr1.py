#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A class to represent calendar dates
#
# name: Sarah Larbi
# email: slarbi@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Sheryn Chung
# partner's email:sherync@bu.edu
#

class Date:
    """A class that stores and manipulates dates,
       represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """The constructor for objects of type Date."""
        self.month = new_month
        self.day = new_day
        self.year = new_year


    # The function for the Date class that returns a Date
    # object in a string representation.
    def __str__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    def is_leap_year(self):
        """ Returns True if the calling object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False


    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 1 below. ####

#1.
    def tomorrow(self):
        """changes the called object so that it represents one calendar day after the date that it originally represented."""

        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_in_month[2] = 29

    #Advance self.day, self.month, and self.year as needed.
        if (self.day + 1) <= days_in_month[self.month]:
            self.day += 1

        elif (self.day + 1) > days_in_month[self.month]:
            self.month += 1
            self.day = 1

            if (self.month+1) > 13:
                self.year += 1
                self.month -= 12
#2.
    def add_n_days(self, n):
        """changes the calling object so that it represents n calendar days after the date it originally represented. Additionally, the method should print all of the dates from the starting date to the finishing date, inclusive of both endpoints."""
        print(self)
        while n > 0:
            self.tomorrow()
            n -= 1
            print(self)
       
#3.
    def __eq__(self, other):
        """ returns True if the called object (self) and the argument (other) represent the same calendar date (i.e., if the have the same values for their day, month, and year attributes). Otherwise, this method should return False."""
        return (self.day == other.day and self.month == other.month and self.year == other.year)
    
#4.
    def is_before(self, other):
        """returns True if the called object represents a calendar date that occurs before the calendar date that is represented by other. If self and other represent the same day, or if self occurs after other, the method should return False."""
        if self.year > other.year:
            return False
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month:
                return True
            if self.month > other.month:
                return False
            if self.month == other.month:
                if self.day > other.day:
                    return False
                if self.day < other.day:
                    return True
                if self.day == other.day:
                    return False

#5.
    def is_after(self, other):
        """returns True if the calling object represents a calendar date that occurs after the calendar date that is represented by other. If self and other represent the same day, or if self occurs before other, the method should return False."""
        if self == other:
            return False
        if self.is_before(other) == True:
            return False
        if self.is_before(other) == False:
            return True

#6.
    def diff(self, other):
        """returns an integer that represents the number of days between self and other."""
        n = 0
        new_self = self.copy()
        new_other = other.copy()
        while new_self.is_before(new_other):
                new_self.tomorrow()
                n -= 1
    
        while new_other.is_before(new_self):
                new_other.tomorrow()
                n += 1

        return n

#7.
    def day_of_week(self):
        """returns a string that indicates the day of the week of the Date object that calls it. In other words, the method should return one of the following strings: 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'."""

        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        other = Date(11, 10, 2014)

        if self.diff(other) > 0 or self.diff(other) < 0:
            day = day_of_week_names[self.diff(other) % 7]

        if self.diff(other) == 0:
            day = day_of_week_names[0]

        return day
            






