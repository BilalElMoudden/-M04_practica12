import xml.etree.ElementTree as ET

def create_xml():

    # Crear una instancia de xml.etree.ElementTree
    root = ET.Element("students")

    # Añadir etiquetas hijo a la raíz
    student1 = ET.SubElement(root, "student")
    student2 = ET.SubElement(root, "student")
    student3 = ET.SubElement(root, "student")
    student4 = ET.SubElement(root, "student")
    student5 = ET.SubElement(root, "student")

    # Añadir etiquetas sub hijos a los hijos
    name1 = ET.SubElement(student1, "name")
    surname1 = ET.SubElement(student1, "surname")
    email1 = ET.SubElement(student1, "email")
    dni1 = ET.SubElement(student1,"dni")

    name2 = ET.SubElement(student2, "name")
    surname2 = ET.SubElement(student2, "surname")
    email2 = ET.SubElement(student2, "email")
    dni2 = ET.SubElement(student2, "dni")

    name3 = ET.SubElement(student3, "name")
    surname3 = ET.SubElement(student3, "surname")
    email3 = ET.SubElement(student3, "email")
    dni3 = ET.SubElement(student3, "dni")

    name4 = ET.SubElement(student4, "name")
    surname4 = ET.SubElement(student4, "surname")
    email4 = ET.SubElement(student4, "email")
    dni4 = ET.SubElement(student4, "dni")

    name5 = ET.SubElement(student5, "name")
    surname5 = ET.SubElement(student5, "surname")
    email5 = ET.SubElement(student5, "email")
    dni5 = ET.SubElement(student5, "dni")

    # Añadir texto a las etiquetas hijo
    name1.text = "John"
    surname1.text = "Doe"
    email1.text = "john@gmail.com"
    dni1.text = "12345678A"

    name2.text = "Javier"
    surname2.text = "Xiaomi"
    email2.text = "javier@gmail.com"
    dni2.text = "87654321B"

    name3.text = "Maria"
    surname3.text = "Martinez"
    email3.text = "maria@gmail.com"
    dni3.text = "47772888A"

    name4.text = "Alice"
    surname4.text = "Fuertes"
    email4.text = "alice@gmail.com"
    dni4.text = "44563421Z"

    name5.text = "Andrea"
    surname5.text = "Ponce"
    email5.text = "andrea@gmail.com"
    dni5.text = "54316434A"

    # Crear un archivo xml
    tree = ET.ElementTree(root)

    root = tree.getroot()
    for element in root:
        element.set('type', 'student')
    tree.write('students.xml')
<<<<<<< HEAD
    tree = ET.parse('students.xml')
    ET.dump(root)

    tree.write('students.xml')



=======
    tree = ET.parse('student.xml')
    ET.dump(root)

    tree.write('student.xml')



create_xml()
>>>>>>> rama_angelo
