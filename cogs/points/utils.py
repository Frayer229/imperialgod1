import json 

async def get_points():
    with open("./data/points.json", "r") as f:
        points = json.load(f)
    return points 

async def get_crown(guild):
    points = await get_points()
    if str(guild.id) not in points:
        return False 
    
    else:
        return points[str(guild.id)]["crown"]

async def create_crown(guild, role):
    points = await get_points()
    if str(guild.id) not in points:
        points[str(guild.id)] = {}
        points[str(guild.id)]["crown"] = role.id
    
    else:
        return False
    
    with open("./data/points.json", "w") as f:
        json.dump(points, f)
    
    return int(points[str(guild.id)]["crown"])

async def find_crown_member(guild):
    pass

async def give_crown_role(guild, member):
    pass 