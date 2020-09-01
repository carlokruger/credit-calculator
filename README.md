# Credit Calculator

## Stage 1/4: Beginning
### Description
Let's stop and think for a second: what should a basic credit calculator do? In general, it is supposed to take several parameters such as credit principal and credit interest, calculate the needed values (for example, monthly payment or overpayment), and output them.

If you are not familiar with these financial concepts, don't worry! We'll explain them in simpler terms. A principal is the original amount of money you get on credit. An interest is the charge you pay for borrowing money, usually calculated as a percentage of the loan sum.

### Objective
Let's start by imitating this basic behavior. There are some prepared variables in the source code that are ready for use: these are the text messages that our credit calculator could output. At this stage, all you need to do is output them in the right order.

### Example
Output:
```
Credit principal: 1000
Month 1: repaid 250
Month 2: repaid 250
Month 3: repaid 500
The credit has been repaid!
```

## Stage 2/4: Dreamworld
### Description
If you found the previous stage too easy, let's move on to something more interesting. The best credits are probably those with a 0% interest; such credits are called installments.

Let's make some calculations for the installments. The user might know the number of periods (months) and want to calculate the monthly payment. Or, the user might know the amount of monthly payment and wonder how many periods it would take to repay the installments.

At this stage, the user should be prompted to input the credit principal. Then, the user should indicate what needs to be calculated (the monthly payment or the number of months) and enter the necessary parameter. After that, the credit calculator should calculate and output the value that the user wants to know.

Not all the resulting numbers will be neat and round. Let’s assume that we don't care about the digits after the dot. If you get a floating-point expression as a result of the calculation, you’ll have to take some additional steps. Take a look at Example 4 in the section "Examples". There, you need to calculate the monthly payment. You know that the credit principal is 1000 and you want to pay it in 9 months. The payment can be calculated like this:

payment=principal / months = 1000 / 9=111.11...

Of course, you can’t pay that exact amount of money. You'll have to round it up and make it 112. Remember that no payment can be more than a monthly payment. If you make a monthly payment of 111, the last payment will be 112, and if you make a monthly payment of 112, the last payment will be 104, which is okay by the rules. You can calculate the last payment with this formula:

lastpayment = principal−(periods−1) * payment = 1000 − 8 * 112 = 104

At this stage, you need to count the number of months or the monthly payment. If the last payment differs from the rest, the program should display both the monthly payment and the last payment.

### Objectives
Your program should do the following:

1. Prompt the user to enter their credit principal and choose one of the two parameters: a number of months or a monthly payment;
2. Ask for the missing value to perform further calculations;
3. Finally, output the results.

### Examples

#### Example 1:
```
Enter the credit principal:
1000
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
m
Enter the monthly payment:
150

It will take 7 months to repay the credit
```
#### Example 2:
```
Enter the credit principal:
1000
What do you want to calculate? 
type "m" for number of monthly payments,
type "p" for the monthly payment:
m
Enter the monthly payment:
1000

It will take 1 month to repay the credit
```
#### Example 3:
```
Enter the credit principal:
1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
p
Enter the number of months:
10

Your monthly payment = 100
```
#### Example 4:
```
Enter the credit principal:
1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment
p
Enter the number of months:
9

Your monthly payment = 112 and the last payment = 104.
```