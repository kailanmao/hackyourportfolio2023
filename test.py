def display_paragraph(paragraph, line_length=50):
    lines = []
    current_line = ""
    
    for line in paragraph.splitlines():
        words = line.split()
        for word in words:
            if len(current_line) + len(word) + 1 <= line_length:
                current_line += word + " "
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        
        if current_line:
            lines.append(current_line.strip())
            current_line = ""
    
    for line in lines:
        print(line)