import PyPDF2

def upload_pdf_file(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        text = ""
        for page in range(num_pages):
            text += reader.getPage(page).extractText()
        return text
        
def find_answer(text, question):
    lines = text.split('\n')
    for line in lines:
        if question.lower() in line.lower():
            return line.strip()
    return "No answer found."
    
def main():
    # Ask the user for the PDF file path
    pdf_file_path = input("Enter the PDF file path: ")

    # Upload the PDF file and extract the text content
    pdf_text = upload_pdf_file(pdf_file_path)

    # Ask the user for a question
    question = input("Enter your question: ")

    # Find an answer to the question
    answer = find_answer(pdf_text, question)
    print(answer)

main()