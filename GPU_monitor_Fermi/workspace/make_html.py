# Read the NVIDIA-SMI output from a text file and convert it to HTML

# Define the path to the text file
input_file_path_121 = './log/10.202.82.121.txt'
input_file_path_13 = './log/10.202.82.13.txt'
input_file_path_12 = './log/10.202.82.12.txt'
input_file_path_Ly = './log/10.204.227.43.txt'
input_file_path_kgl = './log/10.204.227.44.txt'
input_file_path_fer = './log/10.204.227.42.txt'
output_file_path = './log/nvidia_smi_output.html'

# Read the content of the text file
with open(input_file_path_121, 'r') as file:
    content = file.readlines()
    
with open(input_file_path_13, 'r') as file:
    content2 = file.readlines()

with open(input_file_path_12, 'r') as file:
    content3 = file.readlines()

with open(input_file_path_Ly, 'r') as file:
    content4 = file.readlines()

with open(input_file_path_kgl, 'r') as file:
    content5 = file.readlines()

with open(input_file_path_fer, 'r') as file:
    content6 = file.readlines()

# Initialize variables to store different sections of the output
header_info = []
gpu_info = []
process_info = []
current_section = None

# Parse the content of the file
for line in content:
    stripped_line = line.strip()
    if stripped_line.startswith("+---"):
        # Determine the section based on the line content
        if 'Processes:' in stripped_line:
            current_section = 'processes'
        elif 'GPU  Name' in stripped_line:
            current_section = 'gpu'
        else:
            current_section = None
    elif current_section == 'gpu':
        gpu_info.append(stripped_line)
    elif current_section == 'processes':
        process_info.append(stripped_line)
    else:
        header_info.append(stripped_line)
header_info.append(stripped_line)


header_info2 = []
gpu_info2 = []
process_info2 = []
current_section2 = None

# Parse the content of the file
for line in content2:
    stripped_line = line.strip()
    if stripped_line.startswith("+---"):
        # Determine the section based on the line content
        if 'Processes:' in stripped_line:
            current_section2 = 'processes'
        elif 'GPU  Name' in stripped_line:
            current_section2 = 'gpu'
        else:
            current_section2 = None
    elif current_section2 == 'gpu':
        gpu_info2.append(stripped_line)
    elif current_section2 == 'processes':
        process_info2.append(stripped_line)
    else:
        header_info2.append(stripped_line)
header_info2.append(stripped_line)

header_info3 = []
gpu_info3 = []
process_info3 = []
current_section3 = None

# Parse the content of the file
for line in content3:
    stripped_line = line.strip()
    if stripped_line.startswith("+---"):
        # Determine the section based on the line content
        if 'Processes:' in stripped_line:
            current_section3 = 'processes'
        elif 'GPU  Name' in stripped_line:
            current_section3 = 'gpu'
        else:
            current_section3 = None
    elif current_section3 == 'gpu':
        gpu_info3.append(stripped_line)
    elif current_section3 == 'processes':
        process_info3.append(stripped_line)
    else:
        header_info3.append(stripped_line)
header_info3.append(stripped_line)

header_info4 = []
gpu_info4 = []
process_info4 = []
current_section4 = None

# Parse the content of the file
for line in content4:
    stripped_line = line.strip()
    if stripped_line.startswith("+---"):
        # Determine the section based on the line content
        if 'Processes:' in stripped_line:
            current_section4 = 'processes'
        elif 'GPU  Name' in stripped_line:
            current_section4 = 'gpu'
        else:
            current_section4 = None
    elif current_section4 == 'gpu':
        gpu_info4.append(stripped_line)
    elif current_section4 == 'processes':
        process_info4.append(stripped_line)
    else:
        header_info4.append(stripped_line)
header_info4.append(stripped_line)

header_info5 = []
gpu_info5 = []
process_info5 = []
current_section5 = None

# Parse the content of the file
for line in content5:
    stripped_line = line.strip()
    if stripped_line.startswith("+---"):
        # Determine the section based on the line content
        if 'Processes:' in stripped_line:
            current_section5 = 'processes'
        elif 'GPU  Name' in stripped_line:
            current_section5 = 'gpu'
        else:
            current_section5 = None
    elif current_section5 == 'gpu':
        gpu_info5.append(stripped_line)
    elif current_section5 == 'processes':
        process_info5.append(stripped_line)
    else:
        header_info5.append(stripped_line)
header_info5.append(stripped_line)


# Create the HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="3">
    <title>NVIDIA-SMI Output</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            display: flex;
            justify-content: center; /* Center the content horizontally */
            padding: 20px;
        }
        .container {
            display: flex;
            flex-direction: column;
            width: 100%;
        }
        .server-section {
            padding: 20px;
            border: 1px solid #ddd;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .header {
            font-size: 1.0em;
            line-height: 2px;
        }
        table { 
            width: 100%; 
            border-collapse: collapse; 
            margin-bottom: 20px; 
        }
        th, td { 
            border: 1px solid #dddddd; 
            text-align: left; 
            padding: 8px; 
        }
        th { 
            background-color: #f2f2f2; 
        }
        .title { 
            font-size: 1.2em; 
            font-weight: bold; 
        }
        @media (min-width: 1200px) {
            .container {
                flex-direction: row;
                flex-wrap: wrap;
                justify-content: space-between;
            }
            .left-column, .right-column {
                flex: 1;
                min-width: 48%; /* Ensure there's space between columns */
            }
            .right-column {
                margin-left: 20px; /* Add some space between columns */
            }
            .server-section {
                margin-bottom: 0; /* Remove bottom margin for inline display */
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="left-column">
            <div class="server-section">
"""

# Add the header info to the HTML
html_content += '<div class="header">\n'
html_content += '    <pre><h2>新サーバー (10.202.82.121)</h2></pre>\n'
for n, line in  enumerate(header_info):
    if n==0 or n==1:
        html_content += f'    <pre><h3>{line}</h3></pre>\n'
    if n ==16:
        html_content += f'    <pre> </pre>\n'
    if n==3 or n==16 :
        html_content+=  '    <pre>+-----------------------------------------------------------------------------------------+</pre>\n' 
    if n==12 or n==15:
        html_content+=  '    <pre>+-----------------------------------------+------------------------+----------------------+</pre>\n' 
    if n!=0 and n!=1:
        html_content += f'    <pre>{line}</pre>\n'

html_content += '       </div>\n'
html_content += '    </div>\n'
html_content += '    <pre> </pre>\n'
html_content += '    <div class="server-section">\n'
html_content += '       <div class="header">\n'

html_content += f'    <pre><h2>簡易サーバー (10.202.82.13)</h2></pre>\n'

for n, line in  enumerate(header_info2):
    if n==0 or n==1:
        html_content += f'    <pre><h3>{line}</h3></pre>\n'
    if n ==16:
        html_content += f'    <pre> </pre>\n'
    if n==3 or n==16 :
        html_content+=  '    <pre>+-----------------------------------------------------------------------------------------+</pre>\n' 
    if n==12 or n==15:
        html_content+=  '    <pre>+-----------------------------------------+------------------------+----------------------+</pre>\n' 
    if n!=0 and n!=1:
        html_content += f'    <pre>{line}</pre>\n'

html_content += '       </div>\n'
html_content += '    </div>\n'
html_content += '    <pre> </pre>\n'
html_content += '    <div class="server-section">\n'
html_content += '<div class="header">\n'
html_content += '    <pre><h2>Kaggle_VM (10.204.227.44)  </h2></pre>\n'
for n, line in  enumerate(header_info5):
    
    if n==10:
        html_content+=  '    <pre>+-------------------------------+----------------------+----------------------+</pre>\n' 
        html_content += f'    <pre> </pre>\n'
        
    if n==10 :
        html_content+=  '    <pre>+-----------------------------------------------------------------------------------------+</pre>\n' 
    
    if n==1 :
        html_content+=  '    <pre>+-----------------------------------------------------------------------------------------+</pre>\n'
         
    
   
    html_content += f'    <pre>{line}</pre>\n'
    html_content += '    <pre><h2>現在メンテナンス中 復旧予定 未定</h2></pre>\n'

html_content += '       </div>\n'
html_content += '    </div>\n'




html_content += '    </div>\n'
html_content += '     <div class="right-column">\n'
html_content += '     <div class="server-section">\n'
html_content += '     <div class="header">\n'

html_content += f'    <pre><h2>旧サーバー (10.202.82.12)</h2></pre>\n'

for n, line in  enumerate(header_info3):
    if n==0 or n==1:
        html_content += f'    <pre><h3>{line}</h3></pre>\n'
    if n ==22 :
        html_content += f'    <pre> </pre>\n'
    if n==3 or n==22 :
        html_content+=  '    <pre>+-----------------------------------------------------------------------------------------+</pre>\n' 
    if n==12 or n==15 or n==18 or n==21:
        html_content+=  '    <pre>+-----------------------------------------+------------------------+----------------------+</pre>\n' 
    if n!=0 and n!=1:
        html_content += f'    <pre>{line}</pre>\n'



html_content += '       </div>\n'
html_content += '    </div>\n'

html_content += '    <pre> </pre>\n'
html_content += '    <div class="server-section">\n'
html_content += '<div class="header">\n'
html_content += '    <pre><h2>Lyon専有 (10.204.227.43)</h2></pre>\n'
for n, line in  enumerate(header_info4):
    if n==0 or n==1:
        html_content += f'    <pre><h3>{line}</h3></pre>\n'
    
    if n==12:
        html_content+=  '    <pre>+-------------------------------+----------------------+----------------------+</pre>\n' 
        html_content += f'    <pre> </pre>\n'
        html_content+=  '    <pre>+-----------------------------------------------------------------------------------------+</pre>\n' 
    
    if n==3 :
        html_content+=  '    <pre>+-----------------------------------------------------------------------------+</pre>\n' 
    
    if n!=0 and n!=1:
        html_content += f'    <pre>{line}</pre>\n'
    
# html_content += f'    <pre>{line}</pre>\n'


html_content += '       </div>\n'
html_content += '    </div>\n'
html_content += '    <pre> </pre>\n'


html_content += '    <div class="server-section">\n'
html_content += '<div class="header">\n'
html_content += '    <pre><h2>Fermiサーバ (CPU専用) (10.204.227.42)</h2></pre>\n'
for n, line in  enumerate(content6):
    if n==0 or n==1:
        html_content += f'    <pre><h3>{line}</h3></pre>\n'
    if n!=0 and n!=1:
        html_content += f'    <pre>{line}</pre>\n'
 
    
html_content += '       </div>\n'
html_content += '    </div>\n'




# Close the HTML structure
html_content += """
    </div>
    </div>
</body>
</html>
"""

# Write the HTML content to the output file
with open(output_file_path, 'w') as file:
    file.write(html_content)

print(f"HTML content has been saved to {output_file_path}")
