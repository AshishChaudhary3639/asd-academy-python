from openpyxl import Workbook

# Create a new workbook and select the active sheet
wb = Workbook()
sheet = wb.active

# Add headers
sheet['A1'] = "Name"
sheet['B1'] = "Marks"
sheet['C1']="Roll"

# Add some student data
data = [("Ali", 85,12), ("Sara", 90,18), ("John", 78,97)]

for i, (name, marks,Roll) in enumerate(data, start=2):
    sheet[f"A{i}"] = name
    sheet[f"B{i}"] = marks
    sheet[f"C{i}"] = Roll

# Save the file
wb.save("students.xlsx")

# python -m venv venv
# venv\Scripts\activate
