import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import smtplib
from email.message import EmailMessage
import os

# Step 1: Scrape news headlines
url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract top headlines (adjust based on actual site structure)
headlines = soup.select('h3')[:10]  # Get first 10 <h3> tags

# Step 2: Write to Excel
wb = Workbook()
ws = wb.active
ws.title = "Top Headlines"
ws.append(["S.No", "Headline"])

for i, h in enumerate(headlines, start=1):
    ws.append([i, h.get_text(strip=True)])

file_name = "news_headlines.xlsx"
wb.save(file_name)

# Step 3: Email the Excel file
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TO_EMAIL = "recipient_email@example.com"

msg = EmailMessage()
msg['Subject'] = "Top News Headlines"
msg['From'] = EMAIL_ADDRESS
msg['To'] = TO_EMAIL
msg.set_content("Find attached the top news headlines for today.")

# Attach Excel file
with open(file_name, 'rb') as f:
    msg.add_attachment(f.read(), maintype='application', subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=file_name)

# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("Headlines scraped, saved to Excel, and emailed successfully!")
