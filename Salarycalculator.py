def salary(l,wages):
        """Calculate salary - Weekly working hours are given in form of a list."""
        sum=0
        for x in l:
            sum=sum+x
        sal = sum*wages
        return sal

l=[int(x) for x in input("Enter the hours per day in entire week , separated by spaces ").split()]
wages = int(input("Enter the hourly wages"))
print(salary(l,wages))