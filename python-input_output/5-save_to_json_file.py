#!/usr/bin/python3
"""
jtrtyuikmuytrfcvxfdsyuikxm
ldirfytgdhjsdfhgeywuieurytyeuiufrye
oxkmncbvncbvnsjedjfgfhdejwke
"""
import json

def save_to_json_file(my_obj, filename):

    """
    JHGFDERTYUIKNV KYTREDFGUYT
    MNBVCXRTY fdfyuiotfgh
    jytreshgfrtyuiolkmnbvcd
    """
    with open(filename, 'w') as f:
        
        if isinstance(my_obj, set):
            my_obj = list(my_obj)
        json.dump(my_obj, f)
