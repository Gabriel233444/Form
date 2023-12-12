import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server and port
    server.starttls()
    server.login('example@gmail.com', 'password')  # Replace with your credentials
    print('Connected successfully!')
    server.quit()
except Exception as e:
    print('Connection failed:', e)