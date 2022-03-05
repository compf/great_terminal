class ManPageParser:
    def __init__(self,man_page_text) -> None:
        self.man_page_text=man_page_text
    def parse(self):
        lines=self.man_page_text.split("\n")
        my_it=iter(lines)
        while True:
            line=next(my_it)
            if line.startswith("SYNOPSIS"):
                print("syn")
                self.parse_synopsis(my_it)
            if line.startswith("DESCRIPTION"):
                print("dexcr")
                self.parse_description(my_it)
    def parse_synopsis(self,my_it):
        pass
    def parse_description(self,my_it):
        pass