import re
import PyPDF2
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def extract_info_from_pdf(pdf_path, pages=None):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        if pages is None:
            pages = range(len(reader.pages))  

        for page_num in pages:
            if page_num < len(reader.pages):
                page = reader.pages[page_num]
                text += page.extract_text()
            else:
                print(f"Page number {page_num} is out of range.")
    

    org_pattern = re.compile(
        r"([A-Z\s]+)\n"                # Ethnic Group
        r"(.*?)\n"                     # Organization
        r"Website:\s*(.*?)\s*"         # Website
        r"Contact:\s*(.*?),\s*(.*?)\s*" # Contact Name and Position
        r"Phone:\s*([\d\-\,\s]+)\s*"   # Phone Numbers
        r"Email:\s*(.*?)\s*"           # Email
        r"Location:\s*(.*?)\s*\n",     # Location
        re.DOTALL
    )

    matches = org_pattern.findall(text)

    data = []
    for match in matches:
        ethnic_group, organization, website, full_name, position, phone, email, location = match

        name_parts = full_name.split()
        first_name = name_parts[0] if len(name_parts) > 0 else ''
        last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''
        
        phone_numbers = [num.strip() for num in phone.split(',')]

        data.append({
            'Ethnic Group': ethnic_group.strip(),
            'Organization': organization.strip(),
            'First Name': first_name.strip(),
            'Last Name': last_name.strip(),
            'Position': position.strip(),
            'Phone': ', '.join(phone_numbers),
            'Email': email.strip(),
            'Location': location.strip(),
            'Website': website.strip()
        })

    return data

def save_to_google_sheets(data, sheet_name, creds_file):

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)

    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).sheet1

    headers = ['Ethnic Group', 'Organization', 'First Name', 'Last Name', 'Position', 'Phone', 'Email', 'Location', 'Website']
    sheet.clear()  
    sheet.append_row(headers) 

    for row in data:
        sheet.append_row([
            row['Ethnic Group'],
            row['Organization'],
            row['First Name'],
            row['Last Name'],
            row['Position'],
            row['Phone'],
            row['Email'],
            row['Location'],
            row['Website']
        ])

pdf_path = '/Users/kameronvirk/Downloads/EMS.pdf'
sheet_name = 'Directory'
creds_file = '/Users/kameronvirk/Downloads/utility-axis-********.json'


pages_to_extract = [19,20,21]  

data = extract_info_from_pdf(pdf_path, pages=pages_to_extract)


save_to_google_sheets(data, sheet_name, creds_file)

print(f"Data extracted from pages {pages_to_extract} and saved to Google Sheets: {sheet_name}")



