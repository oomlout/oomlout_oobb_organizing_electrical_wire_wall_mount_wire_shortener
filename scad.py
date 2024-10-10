import copy
import opsc
import oobb
import oobb_base

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        #filter = "test"

        kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        kwargs["overwrite"] = True
        
        #kwargs["modes"] = ["3dpr", "laser", "true"]
        kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 12
        kwargs["height"] = 12
        kwargs["thickness"] = 6

    # project_variables
    if True:
        pass
    
    part_default = {} 
    part_default["project_name"] = "test" ####### neeeds setting
    part_default["full_shift"] = [0, 0, 0]
    part_default["full_rotations"] = [0, 0, 0]

    # declare bases
    if False:

        
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        #p3["thickness"] = 6
        part["kwargs"] = p3
        wire_count = 1
        wire_spacing = 15
        wire_diameter = 8
        switchback = 1
        width = 5
        height = 5
        thickness = 12
        kwargs["width"] = width
        kwargs["height"] = height
        kwargs["thickness"] = thickness
        kwargs["wire_count"] = wire_count
        kwargs["wire_spacing"] = wire_spacing
        kwargs["wire_diameter"] = wire_diameter
        kwargs["switchback"] = switchback            
        part["kwargs"] = kwargs
        part["name"] = f"base_{wire_count}_wire_{wire_spacing}_spacing_{wire_diameter}_wire_diameter_{switchback}_switchback"
        #parts.append(part)
        
        part2 = copy.deepcopy(part)
        kwargs2 = copy.deepcopy(kwargs)
        kwargs2["extra"] = "snake"        
        part["kwargs"] = kwargs2
        part["name"] = f"base_{wire_count}_wire_{wire_spacing}_spacing_{wire_diameter}_wire_diameter_{switchback}_switchback"        
        #parts.append(part2)



        wire_diameters = [8,4]
        sizes = []
        
        sizes.append([5,5])
        sizes.append([7,3])
        
        thicknesses = [12,25]

        wire_counts = [1,4]

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
                        part["kwargs"] = copy.deepcopy(kwargs)
                        part["name"] = f"base_{wire_diameter}_wire_diameter_{wire_count}_wire_count"
                        parts.append(part)
    
    #glands
    if True:
                        
        ids = [4,5]
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
            kwargs["extra"] = "gland"
            part["kwargs"] = copy.deepcopy(kwargs)
            part["name"] = f"gland_{id}_id_{od}_od"
            
            parts.append(part)

    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")
            if filter in name:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")


def get_base(thing, **kwargs):

    extra = kwargs.get("extra", "")
    if extra == "snake":
        get_base_snake(thing, **kwargs)
    elif extra == "gland":
        get_gland(thing, **kwargs)
    else:
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

def get_base_snake(thing, **kwargs):

    width = kwargs.get("width", 12)
    depth = kwargs.get("thickness", 4)

    wire_diameter = kwargs.get("wire_diameter", 8)
    wire_spacing = kwargs.get("wire_spacing", 15)

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
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_cylinder"
        p3["radius"] = wire_diameter/2
        dep = 15
        p3["depth"] = dep
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[0] += (width-1)/2 * 15 - 15/2
        pos1[1] += switchback * wire_spacing 
        pos1[2] += dep / 2

        pos2 = copy.deepcopy(pos)
        pos2[0] += -(width-1)/2 * 15 - 15/2
        pos2[1] += -switchback * wire_spacing
        pos2[2] += dep /2

        poss = [pos1,pos2]
        p3["pos"] = poss
        rot1 = [0,90,0]
        p3["rot"] = rot1
        oobb_base.append_full(thing,**p3)

    # add middle pieces
    if True:    
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_cylinder"
        p3["radius"] = wire_diameter/2
        dep = (width - 2) * 15
        p3["depth"] = dep
        #p3["m"] = "#"
        poss = []
        times = switchback + 2
        start_y = -((switchback) * 15)
        for i in range(times):
            pos1 = copy.deepcopy(pos)
            pos1[0] += -dep/2
            pos1[1] += start_y + i * wire_spacing
            pos1[2] += dep / 2
            poss.append(pos1)
        p3["pos"] = poss
        rot1 = [0,90,0]
        p3["rot"] = rot1
        oobb_base.append_full(thing,**p3)

    #add corner pieces
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oring"
        p3["depth"] = wire_diameter
        id = 3.5
        p3["id"] = id
        #p3["m"] = "#"
        poss = []
        pos1 = copy.deepcopy(pos)
        pos1[0] += (width-1)/2 * 15 - 15/2
        pos1[1] += -switchback * wire_spacing/2
        pos1[2] += 0
        poss.append(pos1)
        pos2 = copy.deepcopy(pos)
        pos2[0] += -(width-1)/2 * 15 + 15/2
        pos2[1] += switchback * wire_spacing/2
        pos2[2] += 0
        poss.append(pos2)
        p3["pos"] = poss
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
        shift_y = (width-1)/2 * 15 
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
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
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


###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    try:        
        func = globals()[f"get_{name}"]
        func(thing, **kwargs)
    except:
        get_base(thing, **kwargs)

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        id = thing["id"]
        opsc.opsc_make_object(f'scad_output/{id}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)    


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)