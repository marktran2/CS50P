from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.add_page()
        self.set_font('helvetica', size=50)
        self.cell(0, 60,"CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self.image("shirtificate.png", w=self.epw)
        self.set_font_size(30)
        self.set_text_color(255,255,255)
        self.text(x=55, y=140, txt=f"{name} took CS50")

    def save(self, name):
        self.output(f"{name}.pdf")

def main():
    name = input("Name: ")
    shirtificate = PDF(name)
    shirtificate.save(name)

if __name__ == "__main__":
    main()