# for python 3

import demjson
import sys
import os

# Tree Structure
header = '"id","value"'
result = []
path = []

def recognize(obj):
    if isinstance(obj, list):
        for k in range(len(obj)):
            path.append(str(k))
            result.append('"' + ('.'.join(path)) + '",')
            recognize(obj[k])
            path.pop()
    elif isinstance(obj, dict):
        for k, v in obj.items():
            path.append(str(k))
            result.append('"' + ('.'.join(path)) + '",')
            recognize(v)
            path.pop()
    else:
        result[-1] += ('"' + str(obj) + '"')


def main():
    # File Spec
    file = sys.argv[1]
    filename = sys.argv[1].split('/')[-1].replace('.json','')
    
    # Load File to Variavble: jsondoc
    try:
        print(file)
        with open(file, 'r', encoding='utf-8') as f:
            jsondoc = demjson.decode(f.read())
    except Exception as e:
        exit("Error occurs when loading: '{0}'".format(e))

    # Convert it!
    result.append('"'+filename+'",')
    path.append(filename)
    recognize(jsondoc)
    result.insert(0, header)

    # Write File
    ## Create "output" folder if no exists
    if not os.path.exists(os.path.dirname('./output/')):
        try:
            os.makedirs(os.path.dirname('./output/'))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    ## Write to ./output/output.csv
    try:
        with open('./output/output.csv', 'w') as o:
            o.writelines(map(lambda x: x+"\n", result))
            exit("File conversion was completed without errors.")
    except Exception as e:
        exit("Error occurs when writing: '{0}'".format(e))

if __name__ == "__main__":
    main()
