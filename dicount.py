from datetime import date

dia_semana = date.today().weekday()
semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', "Sabado", 'Domingo')

subtotal = int(input("What's the Subtotal?\n"))
discount = 0
tax = 0

if dia_semana == 1 or dia_semana == 2 and subtotal >= 50:
    discount = subtotal * 0.1
    tax = (subtotal - discount) * 0.06
    subtotal = (subtotal - discount) + tax
    print(f'Discount amount: {discount:.2f}\nSales tax amount: {tax:.2f}\ntotal: {subtotal:.2f}')
else:
    tax = (subtotal - discount) * 0.06
    subtotal = subtotal + tax
    print(f'Sales tax amount: {tax:.2f}\ntotal: {subtotal:.2f}')
    