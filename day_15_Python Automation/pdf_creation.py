from reportlab.pdfgen import canvas

# Create a PDF file
c = canvas.Canvas("Ayush.pdf")
c.setFont("Helvetica", 14)

# Add content
c.drawString(100, 750, "Student Report")
c.drawString(100, 700, "Name: Ayush")
c.drawString(100, 675, "Marks: 92")

# Save the PDF
c.save()

print("PDF generated successfully.")
