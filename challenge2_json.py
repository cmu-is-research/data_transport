import json
import csv
class JSON(object):
    def __init__(self, input_filename):
        self.filename = input_filename
        self.data = None
        
    def loadData(self):
        with open(self.filename) as f:
            self.data = json.load(f)
        
        #makes data a dictionary instead of a one element list
        self.data = self.data[0]

    def getCSV(self, attribute, num, output_filename):
        self.loadData()
        
        #The specific attribute we are looking for: in this case the 
        #attackers list 
        csv_data = self.data[attribute]

        #Checking that a valid attacker is requested
        if(num > len(csv_data)):
            raise ValueError("Invalid attribute request")
        
        #Specific attacker dictionary
        attribute_data = csv_data[num-1]
        
        with open(output_filename, "w", newline="") as file:
            #writer object to write to csv file
            writer = csv.writer(file)
            fields = [] #headers in the csv
            info = [] #data for a specific attacker
            curName = ""

            #function that fills in the relevant data
            self.getData(attribute_data, fields, info, curName)

            #writing data to csv file
            writer.writerow(fields)
            writer.writerow(info)

    def getData(self, curDict, fields, info, curName):
        for key in curDict:
            if(type(curDict[key]) == dict):
                newCurName = curName + key + "_"
                self.getData(curDict[key], fields, info, newCurName)
            else:
                keyName = curName + key
                fields.append(keyName)
                info.append(curDict[key])
                

            