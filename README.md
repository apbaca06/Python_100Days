# Python_100Days
A python practice project



## Day 27: Tkinter, *args, **kwargs and Creating GUI Programs

*args = arguments

**kwargs = keyword arguments

### Tkinter
[Tkinter Documentation](http://tcl.tk/man/tcl8.6/TkCmd/entry.html)
#### Layout Manager
Choose one of the three layout method
1. pack
2. place (precise position)
3. grid

## Day 28:  Tkinter, Dynamic Typing and the Pomodoro GUI Application

### Dynamic Typing
- Strong typing means that the type of a value doesn't change in unexpected ways. A string containing only digits doesn't magically become a number, as may happen in Perl. Every change of type requires an explicit conversion.
- Dynamic typing means that runtime objects (values) have a type, as opposed to static typing where variables have a type.

## Day29: Building a Password Manager GUI App with Tkinter

### Tkinter Message Box
`from tkinter import messagebox`

### Tkinter Widget
- Label
- Button
- Canvas
- Entry

### Clipboard framework: pyperclip

`pyperclip.copy(word)`
`pyperclip.paste()`

## Day 30:  Error   s, Exceptions and JSON Data: Improving the Password
```
    try
    except (if there's error)
    else (no error)
    finally
    
```

## Day 32: Send Email (smtplib) & Manage Dates (datetime)
### smtplib module
```
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        # use \n\n to separate subject and content
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject:Hello\n\nThis is a test email")
```
### datetime module
```
    datetime.now()
```

## Day 33: API Endpoints & API Parameters - ISS Overhead Notifier
### requests module
```
    response = requests.get(url='', params = )
    response.raise_for_status()
    response.json()
```
