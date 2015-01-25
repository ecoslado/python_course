__author__ = 'jesus.pedro.gutierrez.almazan'

def flow_control_if():
    if True:
        print 'es verdad'
    
    if False:
        print 'es verdad'
    else:
        print 'es falso'
    
    knights = ['arturo', 'lancelot', 'robin', 'galahad', 'bedevere']
    if 'patsy' in knights:
        print 'Patsy es un caballero.'
    else:
        print 'Patsy no es un caballero.'
        
    if 'arturo' not in knights:
        print 'Arturo no es un caballero'
    elif 'patsy' in knights:
        print 'patsy es un caballero'
    else:
        print 'Romani ite domum'

def flow_control_for():
    knights = ['arturo', 'lancelot', 'robin', 'galahad', 'bedevere']
    for knight in knights:
        print 'Yo soy %s' % knight.lower().capitalize()
    
    # Iterar sobre una secuencia no conlleva una copia
    # Al iterar sobre una slice se puede modificar la secuencia original
    # Si no se itera sobre un slice entramos en un bucle infinito
    # ya que se itera en orden de aparicion y se modifica la secuencia original
    for knight in knights[:]:
        if knight.lower() == 'galahad':
            knights.insert(0, knight)
    print knights
    
def flow_control_range():
    knights = ['arturo', 'lancelot', 'robin', 'galahad', 'bedevere']
    
    for i in range(5):
        print i
    
    for i in range(2, 5):
        print i
    
    for i in range(len(knights)):
        print i, knights[i]
    
    for i, elem in enumerate(knights):
        print i, elem
    
def flow_control_while():
    knights = ['arturo', 'lancelot', 'robin', 'galahad', 'bedevere']
    while knights[0] != 'bedevere':
        del knights[0]
    print knights

def main():
    flow_control_if()
    flow_control_for()
    flow_control_range()
    flow_control_while()

if __name__ == "__main__":
    main()
