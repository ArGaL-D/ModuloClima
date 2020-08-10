import requests
import sys

try:    
    #Se ingresa un argumento 
    if len(sys.argv) == 2:
            ubicacion = sys.argv[1]
            link_request = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={ubicacion}&appid=0de3a5dac5e0ee0fc2fa8316e5cf3816')
            #Obtenemos el 'json' del sitio. para obtener partes importantes
            info = link_request.json()
            #Si la solictiud da 200 no hubo error en el sitioWeb
            if link_request.status_code == 200:        
                #Temperatura Max - Min
                temperatura = int(info['main']['temp']) # está en 'kelvin'                                
                temp_max = int(info['main']['temp_max'])
                temp_min = int(info['main']['temp_min'])
                celsius = temperatura-273
                fahrenheit = (9*celsius)/5+32
                celsius_max = temp_max-273
                celsius_min = temp_min-273
                fahrenheit_max = (9*celsius_max)/5+32
                fahrenheit_min = (9*celsius_min)/5+32
                
                print(chr(27)+"[1;33m",'[+]',chr(27)+"[0m",'Pais: ',info['sys']['country'])
                print(chr(27)+"[1;33m",'[+]',chr(27)+"[0m",'En:   ',info['name'])
                print(chr(27)+"[1;33m",'[+]',chr(27)+"[0m",'Des:  ',info['weather'][0]['description'],'\n')

                print(chr(27)+"[1;37m",'->',chr(27)+"[0m",'Temperatura: ',temperatura,' ( K )',end=f"  Max: {temp_max}  - Min: {temp_min}\n")
                print(chr(27)+"[1;37m",'->',chr(27)+"[0m",'Temperatura: ',celsius,'  (°C )',end=f"  Max: {celsius_max}   - Min: {celsius_min}\n") 
                print(chr(27)+"[1;37m",'->',chr(27)+"[0m",'Temperatura: ',(fahrenheit),'(°F )',end=f"  Max: {fahrenheit_max} - Min: {fahrenheit_min}\n")        
                print('\n')
            #Hubo error 401 o ERROR 404! - una búsqueda no encontrada
            else:
                print(chr(27)+"[1;31m",'No se encuentra... ',ubicacion,chr(27)+"[0m")                
    else:
        #No se ingresó argumentos al módulo
        print('\n-- Agumentos --')
        print(chr(27)+"[3;31m",'#El modulo debe llevar un argumento',chr(27)+"[0m")
        print(chr(27)+"[1;33m",'[+]',chr(27)+"[0m",'python modulo.py [pais]')
        print(chr(27)+"[1;35m",'[+]',chr(27)+"[0m",'python modulo.py [region/estado/ciudad]')	    
        print(chr(27)+"[1;36m",'Ejemplo ->',chr(27)+"[0m",'python modulo.py Mexico')
        print('\n-- Espacios --')     
        print(chr(27)+"[3;31m",'#Si el argumento lleva espacios usar comillas',chr(27)+"[0m")
        print(chr(27)+"[1;36m",'[+]',chr(27)+"[0m",'python modulo.py ["la region"]')	    
        print(chr(27)+"[1;36m",'Ejemplo ->',chr(27)+"[0m",'python modulo.py "New York" \n')            
except:
    print('\n-> Ha ocurrido un error - NO CONNECTION - ')
