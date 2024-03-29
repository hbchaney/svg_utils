import os
import sys
import re 
from typing import Union
__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
__parent_dir__ = os.path.realpath(os.path.join(__location__, "../.."))

if __parent_dir__ not in sys.path:
    sys.path.insert(0, __parent_dir__)
    
from shape import Shape, Coordinate, Edge, Line

#returns new position as well as either
#str for unaccounted for   
#None for moves
#
class ProcessedCommand: 
    
    def __init__(self, new_position : Coordinate, data : Union[str,Line,None] ) -> None: 
        self.new_position = new_position
        self.data = data
        
    def __str__(self):
        return f'New Coord : {str(self.new_position)} \nExtra data : {str(self.data)}' 
        
class CommandUnit: 
    
    command_maps = {
        'M' : 2, 'm' : 2, 
        'L' : 2, 'l' : 2,
        'H' : 1, 'h' : 1, 
        'V' : 1, 'v' : 1, 
        'C' : 6, 'c' : 6, 
        'S' : 4, 's' : 4,
        'Q' : 4, 'q' : 4, 
        'T' : 2, 't' : 2, 
        'A' : 7, 'a' : 7  
    }
    
    #struct with a command and its associated flags 
    def __init__(self,command : str, flags : list[str]) -> None:
        self.command =  command
        self.flags = flags 
        
    def __str__(self): 
        return f'{self.command} : {self.flags}'
        
         
    def process_command(self, last_position : Coordinate) -> ProcessedCommand: 
        #maps the command to the string
        match self.command.lower():
            case 'm': 
                return self.__m_cmd(last_position)
            case 'h': 
                return self.__h_v_cmd(last_position)
            case 'v': 
                return self.__h_v_cmd(last_position)
            case 'l': 
                return self.__l_cmd(last_position)
            case _: 
                return self.__other_cmd(last_position)
        
    
    def __local_to_global(self,last_pos : Coordinate, local_change : Coordinate): 
        return last_pos + local_change
    
    #### command processes 
    def __m_cmd(self, last_position) -> ProcessedCommand: 
        coord = Coordinate(float(self.flags[0]),
                            float(self.flags[1]))
        if self.command == 'm': 
            coord = self.__local_to_global(coord,last_position)
            
        return ProcessedCommand(coord,None)
        
        
    def __h_v_cmd(self, last_position : Coordinate) -> ProcessedCommand: 
        if self.command == 'h': 
            coord = Coordinate(
                last_position.x + float(self.flags[0]),
                last_position.y
            )
        elif self.command == 'H': 
            coord = Coordinate(
                float(self.flags[0]),
                last_position.y
            )
        elif self.command == 'V': 
            coord = Coordinate(
                last_position.x,
                float(self.flags[0])
            )
        else: # 'v'
            coord = Coordinate(
                last_position.x,
                last_position.y + float(self.flags[0])
            )
            
        return ProcessedCommand(coord,Line(last_position,coord))
    
    def __l_cmd(self,last_position : Coordinate) -> ProcessedCommand:
    
        coord = Coordinate(
            float(self.flags[0]), 
            float(self.flags[1])
        )
        
        if self.command.islower(): 
            coord = self.__local_to_global(last_position,coord)
            
        return ProcessedCommand(coord,Line(last_position,coord))
    
    def __other_cmd(self,last_position : Coordinate) -> ProcessedCommand: 
        
        #last two positions 
        coord = Coordinate(
            float(self.flags[-2]),
            float(self.flags[-1])
        )
        
        if self.command.islower(): 
            coord = self.__local_to_global(last_position,coord)
        
        move_cmd = f'M{last_position.x} {last_position.y}'
        
        output_str = move_cmd + self.command
        for v in self.flags[:-2]: 
            output_str += f' {v}'
            
        output_str += f' {coord.x} {coord.y}'
            
        return ProcessedCommand(coord,output_str)
            
    
def parse_command_str(in_str : str) -> list[CommandUnit]: 
    command_list = [] 
    
    regex_pattern = r'(([a-zA-Z])([^0-9a-zA-Z]*([0-9\.e]+)[^0-9a-zA-Z]*)+)'
    regex_second_pattern = r'[^0-9a-zA-Z\-]*([0-9\.\-e]+)[^0-9a-zA-Z\-]*'
    matches = re.findall(regex_pattern,in_str) 
    
    for m in matches: 
        command = m[0][0]
        second_matches = re.findall(regex_second_pattern,m[0])

        #double or more command condition
        cmd_num = CommandUnit.command_maps[command]
        repeat_num = int(len(second_matches)/ cmd_num)
        for i in range(repeat_num): 
            command_list.append(CommandUnit(command,second_matches[i*cmd_num:cmd_num + i*cmd_num]))
            if command == 'm': 
                command = 'l'
            elif command == 'M': 
                command = 'L'
            
    return command_list

#returns line data and raw path data from other path types
def pull_shape_data(in_str : str, starting_coord : Coordinate = Coordinate(0,0)) -> tuple[list[Line],list[str]]: 
    
    end_data = ([],[])
    current_pos = starting_coord
    cmd_list = parse_command_str(in_str) 
    for cmds in cmd_list: 
        proces_cmd : ProcessedCommand = cmds.process_command(current_pos) 
        current_pos = proces_cmd.new_position
        
        
        if proces_cmd.data is None:
            next
        elif type(proces_cmd.data) == Line: 
            end_data[0].append(proces_cmd.data)
        else: 
            end_data[1].append(proces_cmd.data)
            
    return end_data
            
        
        
    
        
        
        
#tests 
if __name__ == '__main__': 
    test_str = 'm 135.00058,60.000138 h -10.00042 v 4.9997 h -19.99982 v -4.9997 H 90.000232 v 4.9997 h 5.00021 v 9.99989 h -5.00021 v 15.00012 h 5.00021 v 9.99991 h -5.00021 v 5.000222 h 15.000108 v -5.000222 h 19.99982 v 5.000222 h 10.00042 z'
    test_str2 = 'm 134.99983,60.000357 v -10.00043 h -4.99969 v -19.99981 h 4.99969 V 15 h -4.99969 v 5.000213 h -9.99991 V 15 h -15.00012 v 5.000213 h -9.9999 V 15 H 90 v 15.000117 h 5.00021 v 19.99981 H 90 v 10.00043 h 12.49897 a 10,10 0 0 1 9.99991,-10.00043 10,10 0 0 1 10.00042,10.00043 z'
    
    cmd  = parse_command_str(test_str2)
    for v in cmd: 
        print(v)
    print(pull_shape_data(test_str2))
                
            
            
    
    