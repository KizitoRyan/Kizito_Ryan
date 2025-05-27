from multipledispatch import dispatch

class Printer:
    
    @dispatch(str)
    def print(self, content):
        print(f"Printing text: {content}")
    
    @dispatch(list)
    def print(self, documents):
        print("Printing multiple documents:")
        for doc in documents:
            print(f" - {doc}")
    
    @dispatch(dict)
    def print(self, image_data):
        print("Printing image with properties:")
        for key, value in image_data.items():
            print(f"   {key}: {value}")

# A sample object
printer = Printer()

#Test calls of the print() method
printer.print("Hello, world!")  # Prints a single string
printer.print(["Invoice.pdf", "Resume.docx"])  # Prints a list of documents
printer.print({"filename": "photo.jpg", "resolution": "1080p"})  # Prints the dictionary for the image
