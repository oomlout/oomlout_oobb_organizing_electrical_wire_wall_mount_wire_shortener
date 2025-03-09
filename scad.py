import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    oomp_mode = "project"
    #oomp_mode = "oobb"

    if typ == "all":
        filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr", "laser", "true"]
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = False
        #filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]
                
        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = ""
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        wire_diameters = [8,4]        
        #wire_diameters = [4]
        sizes = []
        
        sizes.append([5,5])
        sizes.append([7,3])
        
        thicknesses = [12,25,60,120]
        #thicknesses = [120]

        wire_counts = [0, 1,4]
        #wire_counts = [4]

        for thickness in thicknesses:
            for wire_diameter in wire_diameters:
                for wire_count in wire_counts:
                    for size in sizes:
                        part = copy.deepcopy(part_default)
                        p3 = copy.deepcopy(kwargs)
                        part["kwargs"] = p3
                        width = size[0]
                        height = size[1]
                        kwargs["width"] = width
                        kwargs["height"] = height
                        kwargs["thickness"] = thickness
                        kwargs["wire_count"] = wire_count
                        kwargs["wire_diameter"] = wire_diameter
                        kwargs["extra"] = f"{wire_diameter}_wire_diameter_{wire_count}_wire_count"
                        part["kwargs"] = copy.deepcopy(kwargs)
                        part["name"] = f"end_cap"                        
                        parts.append(part)

                        #add extender
                        if True: #thickness == 25:
                            part = copy.deepcopy(part_default)
                            p3 = copy.deepcopy(kwargs)
                            part["kwargs"] = p3
                            width = size[0]
                            height = size[1]
                            kwargs["width"] = width
                            kwargs["height"] = height
                            kwargs["thickness"] = thickness
                            kwargs["wire_count"] = wire_count
                            kwargs["wire_diameter"] = wire_diameter
                            kwargs["extra"] = f"{wire_diameter}_wire_diameter_{wire_count}_wire_count"
                            part["kwargs"] = copy.deepcopy(kwargs)
                            part["name"] = f"extender"
                            parts.append(part)

                        #add double
                        if True:
                            part = copy.deepcopy(part_default)
                            p3 = copy.deepcopy(kwargs)
                            part["kwargs"] = p3
                            width = size[0]
                            height = size[1]
                            kwargs["width"] = width
                            kwargs["height"] = height
                            kwargs["thickness"] = thickness
                            kwargs["wire_count"] = wire_count
                            kwargs["wire_diameter"] = wire_diameter
                            kwargs["extra"] = f"{wire_diameter}_wire_diameter_{wire_count}_wire_count"
                            part["kwargs"] = copy.deepcopy(kwargs)
                            part["name"] = f"double"
                            parts.append(part)


    #glands
    if True:
                        
        ids = [4,4.5,5]
        od = 8

        for id in ids:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            part["kwargs"] = p3
            width = 1
            height = 1
            kwargs["width"] = width
            kwargs["height"] = height
            kwargs["thickness"] = 12        
            kwargs["wire_diameter"] = od
            kwargs["od"] = od
            kwargs["extra"] = "{id}_id_{od}_od"
            part["kwargs"] = copy.deepcopy(kwargs)
            part["name"] = f"gland"
            
            parts.append(part)


    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        sort.append("wire_count")
        sort.append("wire_diameter")
        
        
        scad_help.generate_navigation(sort = sort)


def get_base(thing, **kwargs):
    print("mistake shouldn't be running")
    import time
    time.sleep(10)

def get_end_cap(thing, **kwargs):
    name = thing.get("id", "default")    
    extra = kwargs.get("extra", "")
    if True:
        width = kwargs.get("width", 12)
        height = kwargs.get("height", 12)
        depth = kwargs.get("thickness", 4)

        wire_diameter = kwargs.get("wire_diameter", 8)
        wire_count = kwargs.get("wire_count", 1)

        prepare_print = kwargs.get("prepare_print", True)

        switchback = kwargs.get("switchback", 1)
        switchback_length = kwargs.get("switchback_length", 45)

        pos = kwargs.get("pos", [0, 0, 0])
        #pos = copy.deepcopy(pos)
        #pos[2] += -20

        #add plate
        if True:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "p"
            p3["shape"] = f"oobb_plate"    
            p3["depth"] = depth
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            pos1[2] += -depth/2
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)
            #add holes
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "p"
            p3["shape"] = f"oobb_holes"
            p3["both_holes"] = True  
            
            p3["holes"] = ["right", "left"]
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)

        #entrance wire pieces
        #wrong height need to make way if spacing isn't 15
        if True:            
            if wire_count == 1:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "negative"
                p3["shape"] = f"oobb_cylinder"
                p3["radius"] = wire_diameter/2
                dep = 15
                p3["depth"] = dep
                #p3["m"] = "#"
                pos1 = copy.deepcopy(pos)
                pos1[0] += (width-1)/2 * 15 - 15/2
                pos1[1] += (height - 3)/2 * 15
                pos1[2] += dep / 2

                pos2 = copy.deepcopy(pos)
                pos2[0] += -(width-1)/2 * 15 - 15/2
                pos2[1] += -(height - 3)/2 * 15
                pos2[2] += dep /2

                poss = [pos1,pos2]
                p3["pos"] = poss
                rot1 = [0,90,0]
                p3["rot"] = rot1
                oobb_base.append_full(thing,**p3)
            else:
            
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "negative"
                p3["shape"] = f"oobb_cylinder"
                p3["radius"] = wire_diameter/2
                dep = 15
                p3["depth"] = dep
                #p3["m"] = "#"
                poss = []
                start_y = -((wire_count-1) * 15)/2
                for i in range(wire_count):
                    pos1 = copy.deepcopy(pos)
                    pos1[0] += (width-1)/2 * 15 - 15/2
                    pos1[1] += start_y + i * 15
                    pos1[2] += dep / 2

                    pos2 = copy.deepcopy(pos)
                    pos2[0] += -(width-1)/2 * 15 - 15/2
                    pos2[1] += start_y + i * 15
                    pos2[2] += dep /2
                    poss.append(pos1)
                    poss.append(pos2)                
                p3["pos"] = poss
                rot1 = [0,90,0]
                p3["rot"] = rot1
                oobb_base.append_full(thing,**p3)
        #add center hollow
        if True:    
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"
            p3["shape"] = f"oobb_plate"    
            p3["width"] = width-0.5
            p3["height"] = height-1.5
            p3["depth"] = depth - 3

            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            pos1[2] += -depth/2 + 1.5
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)

        #join connecting screws in four corners
        if True:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"
            p3["shape"] = f"oobb_screw_countersunk"
            p3["depth"] = depth
            p3["radius_name"] = "m3"
            p3["nut"] = True
            p3["overhang"] = True
            #p3["m"] = "#"
            poss = []
            pos1 = copy.deepcopy(pos)
            pos1[2] += depth/2
            shift_x = (width-1)/2 * 15 - 15/2
            shift_y = (height-1)/2 * 15 
            pos11 = copy.deepcopy(pos1)        
            pos11[0] += shift_x
            pos11[1] += shift_y
            poss.append(pos11)
            pos12 = copy.deepcopy(pos1)
            pos12[0] += -shift_x
            pos12[1] += -shift_y
            poss.append(pos12)
            pos13 = copy.deepcopy(pos1)
            pos13[0] += -shift_x
            pos13[1] += shift_y
            poss.append(pos13)
            pos14 = copy.deepcopy(pos1)
            pos14[0] += shift_x
            pos14[1] += -shift_y
            poss.append(pos14)
            p3["pos"] = poss
            oobb_base.append_full(thing,**p3)

        #add countersunk for wood screws to four corners but in a bit
        if True:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"
            p3["shape"] = f"oobb_screw_countersunk"
            p3["depth"] = depth
            p3["radius_name"] = "m3_screw_wood"
            p3["m"] = "#"
            poss = []
            pos1 = copy.deepcopy(pos)
            pos1[2] += 0
            shift_x = (width-3)/2 * 15 - 15/2
            shift_y = (height-1)/2 * 15 
            pos11 = copy.deepcopy(pos1)        
            pos11[0] += shift_x
            pos11[1] += shift_y
            poss.append(pos11)
            pos12 = copy.deepcopy(pos1)
            pos12[0] += -shift_x
            pos12[1] += -shift_y
            poss.append(pos12)
            pos13 = copy.deepcopy(pos1)
            pos13[0] += -shift_x
            pos13[1] += shift_y
            poss.append(pos13)
            pos14 = copy.deepcopy(pos1)
            pos14[0] += shift_x
            pos14[1] += -shift_y
            poss.append(pos14)
            p3["pos"] = poss
            oobb_base.append_full(thing,**p3)



        if prepare_print:
            #put into a rotation object
            components_second = copy.deepcopy(thing["components"])
            return_value_2 = {}
            return_value_2["type"]  = "rotation"
            return_value_2["typetype"]  = "p"
            pos1 = copy.deepcopy(pos)
            pos1[0] += (width + 1) * 15 
            pos1[2] += 0
            return_value_2["pos"] = pos1
            return_value_2["rot"] = [180,0,0]
            return_value_2["objects"] = components_second
            
            thing["components"].append(return_value_2)

        
            #add slice # top
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_slice"
            pos1 = copy.deepcopy(pos)
            pos1[2] += 0
            p3["pos"] = pos1
            #p3["m"] = "#"
            oobb_base.append_full(thing,**p3)



def get_extender(thing, **kwargs):

    extra = kwargs.get("extra", "")
    width = kwargs.get("width", 12)
    height = kwargs.get("height", 12)
    depth = kwargs.get("thickness", 4)

    wire_diameter = kwargs.get("wire_diameter", 8)
    wire_count = kwargs.get("wire_count", 1)

    prepare_print = kwargs.get("prepare_print", False)

    switchback = kwargs.get("switchback", 1)
    switchback_length = kwargs.get("switchback_length", 45)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add plate
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_plate"    
        p3["depth"] = depth
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += -depth/2
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        
        #add holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True          
        p3["holes"] = ["right", "left"]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

    #entrance wire pieces
    #wrong height need to make way if spacing isn't 15
    if True:            
        if wire_count == 1:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"
            p3["shape"] = f"oobb_cylinder"
            p3["radius"] = wire_diameter/2
            dep = 15
            p3["depth"] = dep
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)
            pos1[0] += (width-1)/2 * 15 - 15/2
            pos1[1] += (height - 3)/2 * 15
            pos1[2] += 0#dep / 2

            pos2 = copy.deepcopy(pos)
            pos2[0] += -(width-1)/2 * 15 - 15/2
            pos2[1] += -(height - 3)/2 * 15
            pos2[2] += 0#dep /2

            poss = [pos1,pos2]
            p3["pos"] = poss
            rot1 = [0,90,0]
            p3["rot"] = rot1
            oobb_base.append_full(thing,**p3)
        else:
        
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"
            p3["shape"] = f"oobb_cylinder"
            p3["radius"] = wire_diameter/2
            dep = 15
            p3["depth"] = dep
            #p3["m"] = "#"
            poss = []
            start_y = -((wire_count-1) * 15)/2
            for i in range(wire_count):
                pos1 = copy.deepcopy(pos)
                pos1[0] += (width-1)/2 * 15 - 15/2
                pos1[1] += start_y + i * 15
                pos1[2] += dep / 2 - depth/2

                pos11 = copy.deepcopy(pos1)
                pos11[2] += depth

                pos2 = copy.deepcopy(pos)
                pos2[0] += -(width-1)/2 * 15 - 15/2
                pos2[1] += start_y + i * 15
                pos2[2] += dep /2 - depth/2

                pos21 = copy.deepcopy(pos2)
                pos21[2] += depth

                poss.append(pos1)
                #poss.append(pos11)
                poss.append(pos2) 
                #poss.append(pos21)               
            p3["pos"] = poss
            rot1 = [0,90,0]
            p3["rot"] = rot1
            oobb_base.append_full(thing,**p3)
    #add center hollow
    if True:    
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_plate"    
        p3["width"] = width-0.5
        p3["height"] = height-1.5
        p3["depth"] = depth

        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += -depth/2
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

    #join connecting screws in four corners
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["depth"] = depth/2
        p3["clearance"] = "top"
        p3["radius_name"] = "m3"
        #p3["nut"] = True
        p3["overhang"] = True
        p3["m"] = "#"
        poss = []
        pos1 = copy.deepcopy(pos)
        pos1[2] += 0
        shift_x = (width-1)/2 * 15 - 15/2
        shift_y = (height-1)/2 * 15 
        pos11 = copy.deepcopy(pos1)        
        pos11[0] += shift_x
        pos11[1] += shift_y
        
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -shift_x
        pos12[1] += -shift_y
        
        pos13 = copy.deepcopy(pos1)
        pos13[0] += -shift_x
        pos13[1] += shift_y
        
        pos14 = copy.deepcopy(pos1)
        pos14[0] += shift_x
        pos14[1] += -shift_y
        #poss.append(pos11)
        #poss.append(pos12)
        poss.append(pos13)
        poss.append(pos14)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

        #add nuts
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_nut"
        p3["radius_name"] = "m3"
        p3["hole"] = True
        p3["clearance"] = "right"
        p3["extra_clearance"] = 0.1
        p3["overhang"] = True
        p3["m"] = "#"
        rot1 = [0,0,90]
        p3["rot"] = rot1
        poss = []
        poss.append(pos11)
        #poss.append(pos12)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

        p4 = copy.deepcopy(p3)
        p4["clearance"] = "left"
        poss = []
        poss.append(pos12)
        p4["pos"] = poss
        oobb_base.append_full(thing,**p4)

    #add countersunk for wood screws to four corners but in a bit
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["depth"] = depth
        p3["radius_name"] = "m3_screw_wood"
        #p3["m"] = "#"
        #p3["clearance"] = "top"
        poss = []
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth/2
        shift_x = (width-3)/2 * 15 - 15/2
        shift_y = (height-1)/2 * 15 
        pos11 = copy.deepcopy(pos1)        
        pos11[0] += shift_x
        pos11[1] += shift_y        
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -shift_x
        pos12[1] += -shift_y        
        pos13 = copy.deepcopy(pos1)
        pos13[0] += -shift_x
        pos13[1] += shift_y        
        pos14 = copy.deepcopy(pos1)
        pos14[0] += shift_x
        pos14[1] += -shift_y
        poss.append(pos11)
        poss.append(pos12)
        poss.append(pos13)
        poss.append(pos14)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

        

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += (width + 1) * 15 
        pos1[2] += 0
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[2] += 0
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


def get_double(thing, **kwargs):

    extra = kwargs.get("extra", "")
    width = kwargs.get("width", 12)
    height = kwargs.get("height", 12)
    depth = kwargs.get("thickness", 4)

    wire_diameter = kwargs.get("wire_diameter", 8)
    wire_count = kwargs.get("wire_count", 1)

    prepare_print = kwargs.get("prepare_print", False)

    switchback = kwargs.get("switchback", 1)
    switchback_length = kwargs.get("switchback_length", 45)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add plate
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_plate"    
        p3["depth"] = depth
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += -depth/2
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        
        #add holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True          
        p3["holes"] = ["right", "left"]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

    #entrance wire pieces
    #wrong height need to make way if spacing isn't 15
    if True:            
        if wire_count == 1:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"
            p3["shape"] = f"oobb_cylinder"
            p3["radius"] = wire_diameter/2
            dep = 15
            p3["depth"] = dep
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)
            pos1[0] += (width-1)/2 * 15 - 15/2
            pos1[1] += (height - 3)/2 * 15
            pos1[2] += 0#dep / 2

            pos2 = copy.deepcopy(pos)
            pos2[0] += -(width-1)/2 * 15 - 15/2
            pos2[1] += -(height - 3)/2 * 15
            pos2[2] += 0#dep /2

            poss = [pos1,pos2]
            p3["pos"] = poss
            rot1 = [0,90,0]
            p3["rot"] = rot1
            oobb_base.append_full(thing,**p3)

            p4 = copy.deepcopy(p3)
            poss = copy.deepcopy(poss)
            for pos1 in poss:
                pos1[2] += depth
            p4["pos"] = poss


        else:
        
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"
            p3["shape"] = f"oobb_cylinder"
            p3["radius"] = wire_diameter/2
            dep = 15
            p3["depth"] = dep
            #p3["m"] = "#"
            poss = []
            start_y = -((wire_count-1) * 15)/2
            for i in range(wire_count):
                pos1 = copy.deepcopy(pos)
                pos1[0] += (width-1)/2 * 15 - 15/2
                pos1[1] += start_y + i * 15
                pos1[2] += dep / 2 - depth/2

                pos11 = copy.deepcopy(pos1)
                pos11[2] += depth

                pos2 = copy.deepcopy(pos)
                pos2[0] += -(width-1)/2 * 15 - 15/2
                pos2[1] += start_y + i * 15
                pos2[2] += dep /2 - depth/2

                pos21 = copy.deepcopy(pos2)
                pos21[2] += depth

                poss.append(pos1)
                #poss.append(pos11)
                poss.append(pos2) 
                #poss.append(pos21)               
            p3["pos"] = poss
            rot1 = [0,90,0]
            p3["rot"] = rot1
            oobb_base.append_full(thing,**p3)

            p4 = copy.deepcopy(p3)
            poss = copy.deepcopy(poss)
            for pos1 in poss:
                pos1[2] += depth
            p4["pos"] = poss
            oobb_base.append_full(thing,**p4)
    #add center hollow
    if True:    
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_plate"    
        p3["width"] = width-0.5
        p3["height"] = height-1.5
        p3["depth"] = depth

        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += -depth/2
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

    #join connecting screws in four corners
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["depth"] = depth/2
        p3["clearance"] = "top"
        p3["radius_name"] = "m3"
        #p3["nut"] = True
        p3["overhang"] = True
        p3["m"] = "#"
        poss = []
        pos1 = copy.deepcopy(pos)
        pos1[2] += 0
        shift_x = (width-1)/2 * 15 - 15/2
        shift_y = (height-1)/2 * 15 
        pos11 = copy.deepcopy(pos1)        
        pos11[0] += shift_x
        pos11[1] += shift_y
        
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -shift_x
        pos12[1] += -shift_y
        
        pos13 = copy.deepcopy(pos1)
        pos13[0] += -shift_x
        pos13[1] += shift_y
        
        pos14 = copy.deepcopy(pos1)
        pos14[0] += shift_x
        pos14[1] += -shift_y
        #poss.append(pos11)
        #poss.append(pos12)
        poss.append(pos13)
        poss.append(pos14)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

        #add nuts
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_nut"
        p3["radius_name"] = "m3"
        p3["hole"] = True
        p3["clearance"] = "right"
        p3["extra_clearance"] = 0.1
        p3["overhang"] = True
        p3["m"] = "#"
        rot1 = [0,0,90]
        p3["rot"] = rot1
        poss = []
        poss.append(pos11)
        #poss.append(pos12)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

        p4 = copy.deepcopy(p3)
        p4["clearance"] = "left"
        poss = []
        poss.append(pos12)
        p4["pos"] = poss
        oobb_base.append_full(thing,**p4)

    #add countersunk for wood screws to four corners but in a bit
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["depth"] = depth
        p3["radius_name"] = "m3_screw_wood"
        #p3["m"] = "#"
        #p3["clearance"] = "top"
        poss = []
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth/2
        shift_x = (width-3)/2 * 15 - 15/2
        shift_y = (height-1)/2 * 15 
        pos11 = copy.deepcopy(pos1)        
        pos11[0] += shift_x
        pos11[1] += shift_y        
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -shift_x
        pos12[1] += -shift_y        
        pos13 = copy.deepcopy(pos1)
        pos13[0] += -shift_x
        pos13[1] += shift_y        
        pos14 = copy.deepcopy(pos1)
        pos14[0] += shift_x
        pos14[1] += -shift_y
        poss.append(pos11)
        poss.append(pos12)
        poss.append(pos13)
        poss.append(pos14)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

        

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += (width + 1) * 15 
        pos1[2] += 0
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[2] += 0
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_gland(thing, **kwargs):
    extra = kwargs.get("extra", "")
    width = kwargs.get("width", 12)
    height = kwargs.get("height", 12)
    depth = kwargs.get("thickness", 4)

    length = 15

    wire_diameter = kwargs.get("wire_diameter", 8)
    
    id = kwargs.get("id", 4)

    #prepare_print = kwargs.get("prepare_print", False)
    prepare_print = kwargs.get("prepare_print", True)

    switchback = kwargs.get("switchback", 1)
    switchback_length = kwargs.get("switchback_length", 45)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add main_cylinder
    clearance = 0.5
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"    
        p3["radius"] = (wire_diameter-clearance)/2
        p3["depth"] = length
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

    #add locking cylinder on top    
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"    
        p3["radius"] = 12/2
        dep = ((length - 15/4)/2) - clearance/2
        p3["depth"] = dep
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)  
        pos1[2] += length/2 - dep/2
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        

    if True:
        #add hole
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_cylinder"    
        p3["radius"] = (id+clearance/2)/2
        p3["depth"] = length
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)



    #add locking pieces
    if True:    
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_cube"
        wid = (wire_diameter + 6)/2
        hei = (depth - 3) 
        dep = ((length - 15/4)/2) - clearance/2
        p3["size"] = [wid,hei,dep]
        #p3["m"] = "#"
        poss = []
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0
        pos1[1] += 0
        pos1[2] += 0
        pos11 = copy.deepcopy(pos1)
        pos11[0] += wid/2
        pos11[2] += length/2 - dep
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -wid/2
        pos12[2] += -length/2
        pos13 = copy.deepcopy(pos1)
        pos13[0] += -wid/2
        pos13[2] += length/2 - dep
        #poss.append(pos11)
        poss.append(pos12)
        #poss.append(pos13)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

    #entrance wire pieces
    #wrong height need to make way if spacing isn't 15
    
    



    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += (width + 1) * 15 
        pos1[2] += 0
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[2] += -500/2
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)