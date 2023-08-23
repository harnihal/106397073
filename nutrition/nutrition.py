fruits= {
    "apple":"130",
    "avocado":"50",
    "sweet cherries":"100",
    "kiwifruit":"90",
    "pear":"100"
}

x = input('Item: ')
x = x.lower()
for calories in fruits:
    if calories == x:
        print('Calories: ', fruits[calories])