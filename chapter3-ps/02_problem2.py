letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''


#=========================#

from datetime import date
# Get today's date
today = date.today()
      
#=========================#


l=input("Enter the name: ")
print(f'''Dear {l},
You are selected!
{today}''')


z=str(today)

print(letter.replace(f"<|Name|>", l).replace(f"<|Date|>", z))

