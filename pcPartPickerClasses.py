import os
dirPath = os.path.dirname(os.path.realpath(__file__))

class PC:
    def __init__(self, PCName:str, CPU:int, Memory:int, Motherboard:str, Graphics:str, PowerSupply:int, Case:str, Price:int):
        self.PCName = PCName
        self.CPU = CPU
        self.Memory = Memory
        self.Motherboard = Motherboard
        self.Graphics = Graphics
        self.PowerSupply = PowerSupply
        self.Case = Case
        self.Price = Price

    def __str__(self):
        return f'{self.PCName} for {self.Price}'
    def toSpecs(self):
        return f'{self.PCName},{str(self.CPU)},{str(self.Memory)},{self.Motherboard},{self.Graphics},{str(self.PowerSupply)},{self.Case}


    def write_pc_specs(pcs:list)->None:
        with open(dirPath + '/specs.pcs', 'w') as file:
            for pc in pcs:
                specs = pc.toSpecs()
                file.write(specs)
                file.write('\n')

    def read_pc_specs():
        pcs = []
        with open(dirPath + '/specs.pcs', 'r') as file:
            for line in file
            line = line.strip()
            if not line:
                return pcs
            specs = line.split(',')
            CPU = specs[0]
            Memory = specs[1]
            Motherboard = specs[2]
            Graphics = specs[3]
            PowerSupply = specs[4]
            Case = specs[5]
            pc = PC(CPU:int, Memory:int, Motherboard:str, Graphics:str, PowerSupply:int, Case:str)
            pcs.append(pc)
        return pcs

    if __name__ == "__main__":
        allPCs = read_pc_specs()
        for pc in allPCs:
            print('Custom PC', pc.CPU,'GHZ', pc.Memory,'GB', pc.Motherboard, pc.Graphcis, pc.PowerSupply,'W', 'in a', pc.Case)
