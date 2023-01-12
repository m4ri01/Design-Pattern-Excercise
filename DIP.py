from enum import Enum
from abc import abstractmethod

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self,name):
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def findAllChildrenOf(self,name):
        pass

class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def addParentChild(self,parent,child):
        self.relations.append((parent,Relationship.PARENT,child))
        self.relations.append((child,Relationship.CHILD,parent))

    def findAllChildrenOf(self,name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2]

class Research:
    # def __init__(self,relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == "John" and r[1] == Relationship.PARENT:
    #             print("John has a child called {}".format(r[2].name))
    def __init__(self,browser):
        relations = browser.findAllChildrenOf("John")
        for c in relations:
            print("John has a child called {}".format(c.name))

John = Person("John")
Lala = Person("Lala")
Roni = Person("Roni")

rl = Relationships()
rl.addParentChild(John,Lala)
rl.addParentChild(John,Roni)

rs = Research(rl)