'''

Create class Container with attributes:
id of type Number
length of type Number
breadth of type Number
height of type Number
pricePerSqrft of type Number

Create the constructor(__init__method) which takes parameters in above sequence for id , length , breadth , height and pricePerSqrFt.

Method will set the values passed as argument to the attributes of the
Container object created.

Create a method find Volume(): This method will calculate the volume of the container as (length*breadth*height) and return it.

Create a class Packaging Company with attributes:
containerList a List of Container objects.

Create the constructor (_init_method) which takes as parameter a list of Containers. Method will set the value passed as argument to the attribute of the Packaging Company object created.

Define two methods as below in the class:

1) find ContainerCost: This method will take as argument a number
representing the id of a Container object and will find the cost of the
Container Object from the containerList of the Packaging Company whose id is equal to the input id passed as argument. The method will return the cost of the container calculated as (volume of container*pricePerSqrFt). If container having the id value passed as argument is not found in the Container list, method returns None. Assume, no two containers have the same id.

2) find Largest Container: This method will find the Container having largest volume from the containerList of the Packaging Company and return the Container object. Assume, not more than one container will have the
largest volume.

These methods should be called from the main section. Instructions to write main section of the code.

a. You would require to write the main section completely. Hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the "sample input description section mentioned below and to read the data in the same sequence.
c. Create the respective objects (Container and arguments to fulfill the __init_ method requirement defined in the respective classes referring to the below instructions.
1. Create a list of Container objects which will be provided to the
Packaging Company object to be created. To create the List
a. Read a number for the count of Container objects to be created and added to the list.
b. Create a container object after reading the data related to it and add the object to the list of Container objects. This point repeats for the number of Container objects to be created (considered in the first line of input) as per point #c1.a.
2. Create Packaging Company object by passing the List of Container objects (created as mentioned in above point #c.1) as the argument.
d. Read a number value as input depicting the container id to be provided
as argument to the method find ContainerCost
e. Call the method find ContainerCost mentioned by passing the id, read in the point #d above from the main section.
g. Display the cost of the container returned by the findContainerCost method. If the method returns None, print the message "No container found" excliding the quotes.

Refer to the sample input and output below for more clarity on inputs and outputs.

h. Call the method find Largest Container and print the id and the volume of the container returned.

You can use/refer the below given sample input and output to verify your solution

Sample input description:
a. The 1st input taken in the main section is the number of Container
objects to be added to the list of containers for the Packaging Company
b. The next set of inputs are the id, length, breadth, height and
pricePerSaret for each Container object taken one after other and is
repeated for number of Container objects given in the first line of input
c. The next line of input is the number representing the id to be supplied as an argument to find ContainerCost method.

You can consider below sample input and output to verify your code.

Input : 
4
101
2
2
2
200
102
3
3
3
120
103
1
2
1
50
104
2
5
1
100
250

Output :
no container found
102 27
'''


class Container:
    def __init_(self, id, length, breadth, height, pricePerSqrFt):
        self.id = id
        self.length = length
        self.breadth = breadth
        self.height = height
        self.pricePerSqrFt = pricePerSqrFt

    def findVolume():
        return self.length*self.breadth*self.height


class PackagingCompany:
    def __init__(self, containerList):
        self.containerList = containerList

    def findContainerCost(self, containerID):
        for container in self.containerList:
            if container.id == containerID:
                return Container.findVolume()*container.pricePerSqrFt
        return None

    def findLargestContainer(self):
        vol = 0
        obj = None
        for con in (self.containerList):
            if(con.findVolume() > vol):
                vol = con.findVolume()
                obj = con
        return obj

if __name__ == '__main__':
    
    