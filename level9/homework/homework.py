#1) დაწერეთ პითონის პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს ორი რიცხვი და შემდეგ დაბეჭდოს მათი ჯამი.

number1 = int(input("Enter number 1:"))
number2 = int(input("Enter number 2:"))
print(number1 + number2)



#2)დაწერეთ პითონის პროგრამა, რომელიც ითვლის მართკუთხედის ფართობს. 
#პროგრამამ უნდა სთხოვოს მომხმარებელსმართკუთხედის სიგანე და სიმაღლე.

area = int(input("Enter the widh of the rectangle:"))
height = int(input("Enter the height of the rectangle:"))
area = (area,height)
print("The area of the rectangle is:",area)

#3) დაწერეთ პითონის პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს ამ რიცხვის ორმაგი.

number = int(input("Enter number:"))
num =int(2)
print(number * num)

#4)დაწერეთ პითონის პროგრამა, რომელიც ითვლის მართკუთხედის პერიმეტრს.
#პროგრამამ უნდა სთხოვოს მომხმარებელს მართკუთხედის სიგანე და სიმაღლე.

lenght = int(input("Enter lenght of rectangle:"))
width = int(input("Enter width of rectamgle:"))
p = 2
result = ((lenght + width)* p )
print(result)

#5) დაწერეთ პითონის პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს რიცხვი და 
#შემდეგ დაბეჭდოს ამ რიცხვის კვადრატი(გამოიყენეთ ** - ოპერატორი)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
result_1 =((num1 + num2) * (num1 + num2))
print(result_1)