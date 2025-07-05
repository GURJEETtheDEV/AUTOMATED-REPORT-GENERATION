import pandas as pd
from fpdf import FPDF

# Step 1: Read data from CSV
df = pd.read_csv("C:/Users/singh/OneDrive/文档/Desktop/data.csv")

# Step 2: Analyze the data
average_score = df['Score'].mean()
max_score = df['Score'].max()
min_score = df['Score'].min()

# Step 3: Create PDF Report
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Student Score Report', ln=True, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Add analysis summary
pdf.cell(0, 10, f'Average Score: {average_score:.2f}', ln=True)
pdf.cell(0, 10, f'Highest Score: {max_score}', ln=True)
pdf.cell(0, 10, f'Lowest Score: {min_score}', ln=True)
pdf.ln(10)

# Add table header
pdf.set_font('Arial', 'B', 12)
pdf.cell(60, 10, 'Name', 1)
pdf.cell(40, 10, 'Score', 1)
pdf.ln()

# Add table rows
pdf.set_font('Arial', '', 12)
for index, row in df.iterrows():
    pdf.cell(60, 10, row['Name'], 1)
    pdf.cell(40, 10, str(row['Score']), 1)
    pdf.ln()

# Save the PDF
pdf.output('C:/Users/singh/OneDrive/文档/Desktop/report.pdf')
print("PDF report generated: report.pdf")
