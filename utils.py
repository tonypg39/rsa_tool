import docker 
import os

# img_base = "moveit/moveit"

def filter_container(img_base,c_id, c_name):
    client = docker.from_env()
    all_ctns = client.containers.list()
    sel_ctns = []
    for c in all_ctns:    
        # print(im.tags[0])
        # print(img_base in im.tags[0])
        if img_base in c.image.tags[0]:
            cn = {
                "id": c.short_id,
                "date": c.attrs['Created'],        
                "status": c.status,
                "name": c.name,
                "image": c.image.tags[0],
                "image_id": c.image.id[7:15],     
            }
            sel_ctns.append(cn)
        
    # Filter the containers to obtain the one
    # If there are no containers active
    if len(sel_ctns) == 0:
        return None 
       
    # Filter the containers to obtain the one
    f_id, f_name = c_id, c_name
    if f_id != '' or f_name != '':
        fsc = [c for c in sel_ctns if (f_id!='' and c['id'].startswith(f_id)) or (f_name!='' and c['name']==f_name)]
        if len(fsc) > 0:
            sc = fsc[0]
        else:
            return None
    else:
        sc = sel_ctns[0]
    
    return sc