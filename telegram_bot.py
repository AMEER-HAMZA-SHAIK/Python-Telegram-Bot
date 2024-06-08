from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6604315761:AAFYY1wfwVyiGsR-panEfKzUdM8-wjrQ5Gc'
BOT_USERNAME = '@mypythonai_bot'

# Dictionary of Python topics with definitions, syntax, and sample programs
python_topics = {
    'variables': {
        'definition': 'Variables in Python are used to store data that can be referenced and manipulated later in the code.',
        'syntax': 'variable_name = value',
        'example': 'x = 10\nprint(x)'
    },
    'data types': {
        'definition': 'Python supports various data types including integers, floats, strings, lists, tuples, and dictionaries.',
        'syntax': 'int: x = 10\nfloat: y = 10.5\nstring: s = "Hello"',
        'example': '''# Integer
x = 10
print(x)

# Float
y = 10.5
print(y)

# String
s = "Hello"
print(s)
'''
    },
    'functions': {
        'definition': 'Functions in Python are defined using the "def" keyword. They are used to encapsulate code for reusability.',
        'syntax': 'def function_name(parameters):\n    # function body',
        'example': '''def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
'''
    },
    'loops': {
        'definition': 'Python supports loops such as "for" and "while". They are used to iterate over sequences or execute a block of code multiple times.',
        'syntax': 'for variable in sequence:\n    # loop body\n\nwhile condition:\n    # loop body',
        'example': '''# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
'''
    },
    'conditionals': {
        'definition': 'Conditionals in Python use "if", "elif", and "else" to execute code based on conditions.',
        'syntax': 'if condition:\n    # code block\nelif condition:\n    # code block\nelse:\n    # code block',
        'example': '''x = 10
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
'''
    },
    'classes': {
        'definition': 'Classes in Python are used to define new data types and create objects. They encapsulate data and functions.',
        'syntax': 'class ClassName:\n    def __init__(self, parameters):\n        # constructor body\n\n    def method_name(self):\n        # method body',
        'example': '''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

p = Person("Alice", 30)
p.greet()
'''
    },
    'modules': {
        'definition': 'Modules in Python are files containing Python code. They are used to organize code into manageable sections.',
        'syntax': 'import module_name\n\nfrom module_name import function_name',
        'example': '''import math

print(math.sqrt(16))

from math import pi
print(pi)
'''
    },
    'exceptions': {
        'definition': 'Exceptions in Python are used to handle errors gracefully. They are managed using try-except blocks.',
        'syntax': 'try:\n    # code block\nexcept Exception as e:\n    # code block\nfinally:\n    # code block',
        'example': '''try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
'''
    }
}

# Define command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm a Python bot. You can ask me about various Python topics or to write simple Python programs for you. Type /help for more info.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I can provide information on Python topics and write simple Python programs for you. For example, you can ask:\n- Write a Hello World program\n- Write a Fibonacci sequence program\n- Write a Factorial program\n- Explain Python variables\n- Explain Python functions\n- Explain Python loops")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")

# Define message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Handle greetings
    if 'hello' in text or 'hi' in text:
        await update.message.reply_text("Hello! How can I assist you with Python today?\n please text me topic name what you want")
        return

    # Handle requests for code snippets
    if 'hello world program' in text:
        code = 'print("Hello, World!")'
        await update.message.reply_text(f"Here is your Hello World program:\n```python\n{code}\n```", parse_mode='Markdown')
        return
    elif 'fibonacci program' in text:
        code = '''def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

fibonacci(10)'''
        await update.message.reply_text(f"Here is your Fibonacci sequence program:\n```python\n{code}\n```", parse_mode='Markdown')
        return
    elif 'factorial program' in text:
        code = '''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))'''
        await update.message.reply_text(f"Here is your Factorial program:\n```python\n{code}\n```", parse_mode='Markdown')
        return
    elif 'prime number checker program' in text:
        code = '''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))'''
        await update.message.reply_text(f"Here is your Prime Number Checker program:\n```python\n{code}\n```", parse_mode='Markdown')
        return
    elif 'palindrome checker program' in text:
        code = '''def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))'''
        await update.message.reply_text(f"Here is your Palindrome Checker program:\n```python\n{code}\n```", parse_mode='Markdown')
        return

    # Handle Python topic explanations
    topic = text.replace('explain ', '').strip()
    if topic in python_topics:
        topic_data = python_topics[topic]
        response = f"**{topic.capitalize()}**\n\n*Definition:*\n{topic_data['definition']}\n\n*Syntax:*\n```python\n{topic_data['syntax']}\n```\n\n*Example:*\n```python\n{topic_data['example']}\n```"
        await update.message.reply_text(response, parse_mode='Markdown')
    else:
        await update.message.reply_text("I don't understand that request. Type /help for available commands.")

# Define error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Register error handler
    app.add_error_handler(error)

    # Start polling
    print("Polling...")
    app.run_polling(poll_interval=3)
