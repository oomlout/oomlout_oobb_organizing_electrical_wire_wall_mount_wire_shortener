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

        #kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        kwargs["overwrite"] = True
        
        kwargs["modes"] = ["3dpr", "laser", "true"]
        #kwargs["modes"] = ["3dpr"]
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
    
    # declare parts
    if True:

        part_default = {} 
        part_default["project_name"] = "test" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        #p3["thickness"] = 6
        part["kwargs"] = p3
        wire_count = 1
        wire_spacing = 15
        wire_diameter = 8
        switchback = 1
        switchback_length = 45
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
        p3["type"] = "p"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["depth"] = depth
        p3["radius_name"] = "m3"
        p3["nut"] = True
        p3["overhang"] = True
        p3["m"] = "#"
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
        opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)    


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)