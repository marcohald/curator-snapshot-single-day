import ruamel.yaml
import subprocess
import os;
program_name = "curator"  

days=14
name='winlogbeat'

yaml = ruamel.yaml.YAML()
file_name = 'input.yaml'
config, ind, bsi = ruamel.yaml.util.load_yaml_guess_indent(open(file_name))
for x in range(99):
    print(x) 
    instances = config['actions']
    instances[1]['options']['name'] = "<curator-"+name+"-{now/d-"+ str(x) +"d}>"
    instances[1]['filters'][0]['value'] = name 
    instances[1]['filters'][1]['unit_count'] = x+days
    instances[1]['filters'][2]['unit_count'] = x+days+1
    
    instances[2]['filters'][0]['value'] = name
    instances[2]['filters'][1]['unit_count'] = x+days
    instances[2]['filters'][2]['unit_count'] = x+days+1


    with open('output.yaml', 'w') as fp:
        yaml.dump(config, fp)
    #break

    os.system("curator --config /storage/curator/curator.yml /root/curator-daily/output.yaml");
    #cont = input("Continue: ")   
    