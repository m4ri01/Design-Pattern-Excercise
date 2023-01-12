#w/o builder create html generator
"""
txt = "hello"
htmlTag = ["<li>",txt,"</li>"]
print(" ".join(htmlTag))

txt = ["hello","world"]
parts = ["</ul>"]
for word in txt:
    parts.append("  <li> {} </li>".format(word))
parts.append("</ul>")
print("\n".join(parts))
"""

#With builder

class HTMLElement:
    indent_size = 2
    def __init__(self,name="",text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self,indent):
        lines = []
        i = " "*(indent*self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " "*((indent+1)*self.indent_size)
            lines.append(f"{i1}{self.text}")
        
        for e in self.elements:
            lines.append(e.__str(indent+1))
        
        lines.append(f"{i}</{self.name}>")
        return '\n'.join(lines)
    
    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HTMLBuilder(name)

    
class HTMLBuilder:
    __root = HTMLElement()

    def __init__(self,root_name):
        self.root_name = root_name
        self.__root.name = root_name

    def add_child(self,child_name,child_text):
        self.__root.elements.append(
            HTMLElement(child_name,child_text)
        )
        return self
    
    def clear(self):
        self.__root = HTMLElement(name=self.root_name)
    
    def __str__(self):
        return str(self.__root)

builder = HTMLElement.create("ul")
builder.add_child("li","hello")
builder.add_child("li","world")
print(builder)