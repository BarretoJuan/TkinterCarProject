import ctypes
from datetime import datetime
from tkinter import *
from tkinter import ttk



#ARRAYS
#Vehiculos
vehiculo_codigo=[]
vehiculo_marca=[]
vehiculo_modelo=[]
vehiculo_anio=[]
vehiculo_km=[]
vehiculo_precio=[]
vehiculo_estatus=[]

#Clientes
cliente_cedula=[]
cliente_tipo=[]
cliente_nombre=[]
cliente_nacimiento=[]
cliente_direccion=[]
cliente_estado=[]

#Ventas
venta_factura=[]
venta_fecha=[]
venta_cedula=[]
venta_codigo_vehiculo=[]
venta_modelo_vehiculo=[]

def read_customers():
    file = open('COMPRADORES.TXT','r')

    cliente_cedula.clear()
    cliente_tipo.clear()
    cliente_nombre.clear()
    cliente_nacimiento.clear()
    cliente_direccion.clear()
    cliente_estado.clear()

    for x in file:
        cliente_cedula.append(x[0:8])
        cliente_tipo.append(x[8])
        cliente_nombre.append(x[9:59])
        cliente_nacimiento.append(x[59:67])
        cliente_direccion.append(x[67:117])
        cliente_estado.append(x[117:133])
    file.close()

def read_sales():
    file = open("VENTAS.TXT",'r')

    venta_factura.clear()
    venta_fecha.clear()
    venta_cedula.clear()
    venta_codigo_vehiculo.clear()
    venta_modelo_vehiculo.clear()

    for x in file:
        venta_factura.append(x[0:5])
        venta_fecha.append(x[5:13])
        venta_cedula.append(x[13:21])
        venta_codigo_vehiculo.append(x[21:24])
        venta_modelo_vehiculo.append(x[24:44])
    file.close()

def read_vehicles():
    file = open('VEHICULOS.TXT','r')

    vehiculo_codigo.clear()
    vehiculo_marca.clear()
    vehiculo_modelo.clear()
    vehiculo_anio.clear()
    vehiculo_km.clear()
    vehiculo_precio.clear()
    vehiculo_estatus.clear()

    for x in file:
        vehiculo_codigo.append(x[0:3])
        vehiculo_marca.append(x[3:23])
        vehiculo_modelo.append(x[23:43])
        vehiculo_anio.append(x[43:47])
        vehiculo_km.append(x[47:53])
        vehiculo_precio.append(x[53:61])
        vehiculo_estatus.append(x[61])
    file.close()




def new_window(title):
    top = Toplevel()
    top.title(title)
    top.state('zoomed')
    top.config(bg="#000b1c")

    main_frame = Frame(top, bg="#000b1c")
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas=Canvas(main_frame, bg="#000b1c")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox('all')))

    second_frame = Frame(my_canvas, bg="#000b1c", padx=(200), pady=50)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    return second_frame


def show_vehicles():

    top = new_window("Mostrar Vehículos")
    columns = ('vehiculo_codigo', 'vehiculo_marca', 'vehiculo_modelo', 'vehiculo_anio', 'vehiculo_km', 'vehiculo_precio', 'vehiculo_estatus')
    tree = ttk.Treeview(top, columns=columns, show='headings')

    tree.heading('vehiculo_codigo', text="Código")
    tree.heading('vehiculo_marca', text="Marca")
    tree.heading('vehiculo_modelo', text="Modelo")
    tree.heading('vehiculo_anio', text="Año")
    tree.heading('vehiculo_km', text="Kilometraje")
    tree.heading('vehiculo_precio', text='Precio')
    tree.heading('vehiculo_estatus', text='Estado')
    column_widths = (100, 100, 150, 80, 100, 120, 80)

    for i, column in enumerate(columns):
        tree.column(column, width=column_widths[i])
        tree.heading(column, text=column)

    read_vehicles()
    for x in range(0, len(vehiculo_codigo)):
        tree.insert('', END, values=(vehiculo_codigo[x], vehiculo_marca[x], vehiculo_modelo[x], vehiculo_anio[x],
                                     vehiculo_km[x], (vehiculo_precio[x][0:6] + "," + vehiculo_precio[x][6:]),
                                     vehiculo_estatus[x]))

    tree.column(columns[-1], stretch=YES)
    tree.pack(fill=BOTH, expand=YES)  

def add_vehicle():
    top_window = new_window("Agregar Vehículo")
    title0 = Label(top_window, text='Agregar Vehículo', anchor="center", font=("Arial", 25, "bold"), bg="#000b1c", fg="#d9dadb")
    title0.pack(pady=(20,20))
    vehicle_brand_label = Label(top_window, text="Marca del Vehículo", justify="left", font=("Arial", 18), bg="#000b1c", fg="#d9dadb" )
    vehicle_brand_label.pack(pady=(0,5))
    vehicle_brand_entry = Entry(top_window, font=("Arial", 18), bg="#000b1c", fg="#d9dadb", justify="left", width=20 )
    vehicle_brand_entry.pack(pady=(0,15))

    vehicle_model_label = Label(top_window, text="Modelo del Vehículo", justify="left", font=("Arial", 18), bg="#000b1c", fg="#d9dadb" )
    vehicle_model_label.pack(pady=(0,5))
    vehicle_model_entry = Entry(top_window, font=("Arial", 18), bg="#000b1c", fg="#d9dadb", justify="left", width=20,)
    vehicle_model_entry.pack(pady=(0,15))

    vehicle_year_label = Label(top_window, text="Año del Vehículo", justify="left", font=("Arial", 18), bg="#000b1c", fg="#d9dadb" )
    vehicle_year_label.pack(pady=(0,5))
    vehicle_year_entry = Entry(top_window, font=("Arial", 18), bg="#000b1c", fg="#d9dadb", justify="left", width=4)
    vehicle_year_entry.pack(pady=(0,15))
    
    vehicle_km_label = Label(top_window, text="Kilometraje del Vehículo", justify="left", font=("Arial", 18), bg="#000b1c", fg="#d9dadb" )
    vehicle_km_label.pack(pady=(0,5))
    vehicle_km_entry = Entry(top_window, font=("Arial", 18), bg="#000b1c", fg="#d9dadb", justify="left", width=6)
    vehicle_km_entry.pack(pady=(0,15))

    vehicle_price_label = Label(top_window, text="Precio del Vehículo (máximo 6 posiciones enteras)", justify="left", font=("Arial", 18), bg="#000b1c", fg="#d9dadb" )
    vehicle_price_label.pack(pady=(0,5))
    vehicle_price_integer_entry = Entry(top_window, font=("Arial", 18), bg="#000b1c", fg="#d9dadb", justify="left", width=6)
    vehicle_price_integer_entry.pack(pady=(0,0))
    vehicle_price_label2 = Label(top_window, text="Precio del Vehículo (máximo 2 posiciones decimales)", justify="left", font=("Arial", 18), bg="#000b1c", fg="#d9dadb" )
    vehicle_price_label2.pack(pady=(0,5))
    vehicle_price_decimal_entry = Entry(top_window, font=("Arial", 18), bg="#000b1c", fg="#d9dadb", justify="left", width=2)
    vehicle_price_decimal_entry.pack(pady=(0,0))

    error_label = Label(top_window, text="Complete los campos, y se detectarán errores",  bg="#000b1c", fg="#d9dadb", anchor="center" )
    error_label.pack(pady=(0,15))

    def validate_add_vehicle():
        error_label.config(text='Complete los campos, y se detectarán errores')
        vehicle_brand = vehicle_brand_entry.get()
        vehicle_model = vehicle_model_entry.get()
        vehicle_year = vehicle_year_entry.get() 
        vehicle_km = vehicle_km_entry.get()
        vehicle_price_integer = vehicle_price_integer_entry.get()
        vehicle_price_decimal = vehicle_price_decimal_entry.get()
      
        # Validación de la marca del vehículo 
        if len(vehicle_brand) > 20:
            error_label.config(text = error_label.cget("text") + "\n La marca del vehículo no puede ser mayor a 20 caracteres")
            brand = False
        
        if vehicle_brand == None or vehicle_brand == "":
            error_label.config(text = error_label.cget("text") + "\n La marca del vehículo no puede estar vacía")
            brand = False
        
        else:
            while len(vehicle_brand) < 20:
                vehicle_brand = vehicle_brand+" "
            brand = True
        # -----------------------------------
        # Validación modelo del vehículo
        if len(vehicle_model) > 20:
            error_label.config(text = error_label.cget("text") + "\n El modelo del vehículo no puede ser mayor a 20 caracteres")
            model = False
        
        if vehicle_model == None or vehicle_model == "":
            error_label.config(text = error_label.cget("text") + "\n El modelo del vehículo no puede estar vacío")
            model = False
        
        else:
            while len(vehicle_model) < 20:
                vehicle_model = vehicle_model+" "
            model = True
        #---------------------------------------------------------------
        # Validación año del vehículo
        if not vehicle_year.isdigit() or len(vehicle_year) != 4:
            year = False
            error_label.config(text = error_label.cget("text") + "\n El año del vehículo debe ser un valor entero de cuatro dígitos")
        
        else:
            year = True
        #--------------------------------------------------------------------------
        # Validacion del kilometraje del vehiculo
        if not vehicle_km.isdigit() or len(vehicle_km) > 6:
            km = False
            error_label.config(text = error_label.cget("text") + "\n El kilometraje del vehículo debe ser un valor entero no mayor de seis dígitos")
        
        else:
            while len(vehicle_km) < 6:
                vehicle_km = "0"+vehicle_km
            km = True       
       #-------------------------------------------------------------------------------------
       # Validación del precio del vehículo
        if not vehicle_price_integer.isdigit() or len(vehicle_price_integer) > 6:
            integer_price = False
            error_label.config(text = error_label.cget("text") + "\n El precio entero del vehículo debe ser un número no mayor de seis dígitos")
        
        else:
            while len(vehicle_price_integer) < 6:
                vehicle_price_integer = "0"+vehicle_price_integer
            integer_price = True    

        if not vehicle_price_decimal.isdigit() or len(vehicle_price_decimal) > 2:
            decimal_price = False
            error_label.config(text = error_label.cget("text") + "\n El precio decimal del vehículo debe ser un número no mayor de dos dígitos")
        
        else:
            while len(vehicle_price_decimal) < 2:
                vehicle_price_decimal = vehicle_price_decimal+"0"
            decimal_price = True   
        #---------------------------------------------------------------------------------------------


        if brand == False or model == False or year == False or km == False or decimal_price == False or integer_price == False:
            error_label.config(text = error_label.cget("text") + "\n Corrija los errores")

        else:
            file = open('VEHICULOS.TXT','a+')
            read_vehicles()
            
            codigo_nuevo = int(len(vehiculo_codigo))+1
            codigo_str = str(codigo_nuevo)
            while len(codigo_str) < 3:
                codigo_str = "0" + codigo_str
            file.write("\n"+str(codigo_str)+vehicle_brand+vehicle_model+vehicle_year+vehicle_km+vehicle_price_integer+vehicle_price_decimal+"0")
            file.close()
            error_label.config(text = "Vehiculo código "+codigo_str+" agregado con éxito")
            
    submit = Button(top_window, bg="black", fg="white", text="Cargar datos", command=validate_add_vehicle)
    submit.pack(pady=(25,0))



def show_sales():
    top = new_window("Mostrar Ventas")
    columns = ("Num. Factura", "Fecha compra", "cedula comprador","codigo vehiculo","modelo vehiculo")
    tree = ttk.Treeview(top, columns=columns, show='headings')

    tree.heading("Num. Factura", text="Num. Factura")
    tree.heading("Fecha compra", text="Fecha compra (DDMMYYYY)")
    tree.heading("cedula comprador", text="Cedula Comprador")
    tree.heading("codigo vehiculo", text="Codigo Vehiculo")
    tree.heading("modelo vehiculo", text="Modelo Vehiculo")
    read_sales()
    for x in range(0,len(venta_factura)):
        tree.insert('', END, values=(venta_factura[x],venta_fecha[x],venta_cedula[x],venta_codigo_vehiculo[x],venta_modelo_vehiculo[x]))
    tree.pack()


def add_sale():
    top_window = new_window("Agregar Ventas")

    buyer_id_label = Label(top_window, text="Cédula Comprador", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    buyer_id_label.pack(pady=(0, 3))
    buyer_id_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=8)
    buyer_id_entry.pack(pady=(0, 10))

    doc_type_label = Label(top_window, text="Tipo de documento (R: Rif,C: Cédula,D: Diplomático,P: Pasaporte)", justify="left", font=("Arial", 12), bg="#000b1c", fg="#d9dadb")
    doc_type_label.pack(pady=(0, 3))
    doc_type_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=2)
    doc_type_entry.pack(pady=(0, 10))

    buyer_name_label = Label(top_window, text="Nombre del comprador", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    buyer_name_label.pack(pady=(0, 3))
    buyer_name_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=50)
    buyer_name_entry.pack(pady=(0, 10))

    birth_day_label = Label(top_window, text="Día de nacimiento", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    birth_day_label.pack(pady=(0, 3))
    birth_day_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=2)
    birth_day_entry.pack(pady=(0, 10))

    birth_month_label = Label(top_window, text="Mes de nacimiento", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    birth_month_label.pack(pady=(0, 3))
    birth_month_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=2)
    birth_month_entry.pack(pady=(0, 10))

    birth_year_label = Label(top_window, text="Año de nacimiento", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    birth_year_label.pack(pady=(0, 3))
    birth_year_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=4)
    birth_year_entry.pack(pady=(0, 10))

    address_label = Label(top_window, text="Dirección", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    address_label.pack(pady=(0, 3))
    address_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=50)
    address_entry.pack(pady=(0, 10))

    state_label = Label(top_window, text="Estado", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    state_label.pack(pady=(0, 3))
    state_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=15)
    state_entry.pack(pady=(0, 10))

    # Venta Section
    sale_title = Label(top_window, text='Insertar Venta', anchor="center", font=("Arial", 20, "bold"), bg="#000b1c", fg="#d9dadb")
    sale_title.pack(pady=(10, 10))

    date_label = Label(top_window, text="Fecha de la compra (DD/MM/YYYY)", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    date_label.pack(pady=(0, 3))
    date_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=15)
    date_entry.pack(pady=(0, 10))

    # Set today's date in the format DD/MM/YYYY
    today_date = datetime.today().strftime('%d%m%Y')
    date_entry.insert(0, today_date)
    date_entry.config(state="enabled")

    vehicle_code_label = Label(top_window, text="Código del Vehículo", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    vehicle_code_label.pack(pady=(0, 3))
    vehicle_code_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=15)
    vehicle_code_entry.pack(pady=(0, 10))

    error_label = Label(top_window, text="Complete los campos, y se detectarán errores",  bg="#000b1c", fg="#d9dadb", anchor="center" )
    error_label.pack(pady=(0,15))

    def validate_add_sale():
        error_label.config(text='Complete los campos, y se detectarán errores')
        buyer_id = buyer_id_entry.get()
        doc_type = doc_type_entry.get()
        buyer_name = buyer_name_entry.get()
        birth_day = birth_day_entry.get()
        birth_month = birth_month_entry.get()
        birth_year = birth_year_entry.get()
        address = address_entry.get()
        state = state_entry.get()
        date = date_entry.get()
        vehicle_code = vehicle_code_entry.get()
    
           # Validation for buyer_id
        if not buyer_id.isdigit() or len(buyer_id) > 8:
            error_label.config(text=error_label.cget("text") + "\n La cedula debe ser numerico y no mayor de 8 digitos")
            buyid=False
        else:
            while len(buyer_id) < 8:
                buyer_id = '0'+buyer_id
            buyid=True
        
        # -----------------------------------

        # Validation for doc_type
 
        if doc_type not in ['R', 'C', 'D', 'P']:
            error_label.config(text=error_label.cget("text") + "\n Tipo de documento no válido. Use R, C, D, o P")
            doc=False
        else:
            doc=True
        # -----------------------------------

        # Validation for buyer_name
        if len(buyer_name) > 50 or buyer_name == '':
            error_label.config(text=error_label.cget("text") + "\n El nombre del comprador no puede ser mayor a 50 caracteres o estar vacio")
            name = False
        else:
            while len(buyer_name) < 50:
                buyer_name = buyer_name + " "
            name=True
        # -----------------------------------

        # Validation for birth_day and birth_month
        if not birth_day.isdigit() or len(birth_day) > 2:
            day = False
            error_label.config(text = error_label.cget("text") + "\n El día de nacimiento no puede ser mayor de dos digitos")
        
        else:
            while len(birth_day) < 2:
                birth_day = "0"+birth_day
            day = True
            
        if not birth_month.isdigit() or len(birth_month) > 2:
            month = False
            error_label.config(text = error_label.cget("text") + "\n El mes de nacimiento no puede ser mayor de dos digitos")
        
        else:
            while len(birth_month) < 2:
                birth_month = "0"+birth_month
            month = True   


        # -----------------------------------

        # Validation for birth_year
        if not birth_year.isdigit() or len(birth_year) != 4:
            error_label.config(text=error_label.cget("text") + "\n El año de nacimiento debe ser un valor entero de cuatro dígitos")
            year= False
        
        else:
            year = True
        # -----------------------------------

        # Validation for address
        if len(address) > 50 or address == '':
            error_label.config(text=error_label.cget("text") + "\n La dirección del comprador no puede ser mayor a 50 caracteres o estar vacio")
            buyer_address = False
        else:
            while len(address) < 50:
                address = address + " "
            buyer_address=True

        # -----------------------------------

        # Validation for state
        if len(state) > 15 or state == '':
            error_label.config(text=error_label.cget("text") + "\n El estado del comprador no puede ser mayor a 15 caracteres o estar vacio")
            buyer_state = False
        else:	
            while len(state) < 15:
                state = state + " "
            buyer_state=True

        # -----------------------------------

        # Validation for date
        date = date_entry.get()
        # -----------------------------------

        # Validation for vehicle_code
        if not vehicle_code.isdigit() or len(vehicle_code) > 3:
           error_label.config(text=error_label.cget("text") + "\n El codigo del vehiculo debe ser un numero no mayor de 3 digitos")
           code = False
        
        else:
            while len(vehicle_code) < 3:
                vehicle_code= '0'+vehicle_code
            code = True

        if buyid == False or doc == False or name == False or day == False or month == False or year == False or buyer_address == False or buyer_state == False or code == False:
            error_label.config(text = error_label.cget("text") + "\n Corrija los errores")

        else:
            read_vehicles()
            read_customers()
            read_sales()
            if vehicle_code in vehiculo_codigo:
                index=vehiculo_codigo.index(vehicle_code)
                car_model = vehiculo_modelo[index]
                if vehiculo_estatus[index] == '0':
                   vehiculo_estatus[index]='1'
                   file = open('COMPRADORES.TXT', "a+")
                   file.write("\n"+buyer_id+doc_type+buyer_name+birth_day+birth_month+birth_year+address+state)
                   file.close()
                   file = open("VEHICULOS.TXT",'w')
                   for x in range(0,len(vehiculo_codigo)):
                       file.write(vehiculo_codigo[x]+vehiculo_marca[x]+vehiculo_modelo[x]+vehiculo_anio[x]+vehiculo_km[x]+vehiculo_precio[x]+vehiculo_estatus[x]+"\n")
                   file.close()

                   file = open('VENTAS.TXT', 'a+')
                   codigo_venta_nuevo = int(len(venta_factura))+1
                   codigo_venta_str = str(codigo_venta_nuevo)
                   while len(codigo_venta_str) <5:
                       codigo_venta_str = "0"+codigo_venta_str
                   file.write("\n"+codigo_venta_str+date+buyer_id+vehicle_code+car_model)
                   file.close()
                   error_label.config(text = "Vehiculo codigo "+vehicle_code+" vendido satisfactoriamente")
                else: 
                    error_label.config(text = "El codigo de vehiculo ya fue vendido")

            else:
                error_label.config(text = "El codigo de vehiculo ingresado no existe")

    submit = Button(top_window, bg="black", fg="white", text="Cargar datos", command=validate_add_sale)
    submit.pack(pady=(5,0))           
                  
     
                           








def sale_by_date():
    top_window = new_window("Ventas por Fecha")
    label = Label(top_window, text="Ventas por fecha", justify="left", font=('Arial',20), bg="#000b1c", fg="#d9dadb")
    label.pack(pady=(5,15))
    birth_day_label = Label(top_window, text="Día", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    birth_day_label.pack(pady=(0, 3))
    birth_day_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=2)
    birth_day_entry.pack(pady=(0, 10))

    birth_month_label = Label(top_window, text="Mes", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    birth_month_label.pack(pady=(0, 3))
    birth_month_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=2)
    birth_month_entry.pack(pady=(0, 10))

    birth_year_label = Label(top_window, text="Año", justify="left", font=("Arial", 16), bg="#000b1c", fg="#d9dadb")
    birth_year_label.pack(pady=(0, 3))
    birth_year_entry = Entry(top_window, font=("Arial", 16), bg="#000b1c", fg="#d9dadb", justify="left", width=4)
    birth_year_entry.pack(pady=(0, 10))

    error_label = Label(top_window, text="Complete los campos, y se detectarán errores",  bg="#000b1c", fg="#d9dadb", anchor="center" )
    error_label.pack(pady=(0,15))

    def validate_date():
        error_label.config(text='Complete los campos, y se detectarán errores')
        birth_day = birth_day_entry.get()
        birth_month = birth_month_entry.get()
        birth_year = birth_year_entry.get()


        if not birth_day.isdigit() or len(birth_day) > 2:
            day = False
            error_label.config(text = error_label.cget("text") + "\n El día no puede ser mayor de dos digitos")
        
        else:
            while len(birth_day) < 2:
                birth_day = "0"+birth_day
            day = True
            
        if not birth_month.isdigit() or len(birth_month) > 2:
            month = False
            error_label.config(text = error_label.cget("text") + "\n El mes no puede ser mayor de dos digitos")
        
        else:
            while len(birth_month) < 2:
                birth_month = "0"+birth_month
            month = True   



        if not birth_year.isdigit() or len(birth_year) != 4:
            error_label.config(text=error_label.cget("text") + "\n El año debe ser un valor entero de cuatro dígitos")
            year= False
        
        else:
            year = True


        if day == False or month == False or year == False:
            error_label.config(text = error_label.cget("text") + "\n Corrija los errores")
        
        else:
            read_sales()
            read_vehicles()
            read_customers()
            date = birth_day+birth_month+birth_year

            if date in venta_fecha:
                
                top_window2 = new_window("Ventas del "+date)
                columns = ("Num. Factura", "Fecha compra", "cedula comprador","codigo vehiculo","modelo vehiculo")
                tree = ttk.Treeview(top_window2, columns=columns, show='headings')

                tree.heading("Num. Factura", text="Num. Factura")
                tree.heading("Fecha compra", text="Fecha compra (DDMMYYYY)")
                tree.heading("cedula comprador", text="Cedula Comprador")
                tree.heading("codigo vehiculo", text="Codigo Vehiculo")
                tree.heading("modelo vehiculo", text="Modelo Vehiculo")
                total = 0
                for x in range(0,len(venta_factura)):
                    if venta_fecha[x] == date:
                        tree.insert('', END, values=(venta_factura[x],venta_fecha[x],venta_cedula[x],venta_codigo_vehiculo[x],venta_modelo_vehiculo[x]))
                        price_index=vehiculo_codigo.index(venta_codigo_vehiculo[x])
                        precio_decimal = float(vehiculo_precio[price_index][0:6]+"."+vehiculo_precio[price_index][6:])
                        total = total+precio_decimal
                tree.pack()

                label = Label(top_window2, text="TOTAL VENDIDO: "+str(total), justify="left", font=('Arial',20), bg="#000b1c", fg="#d9dadb")
                label.pack(pady=10)


            else:
                error_label.config(text="En el día ingresado no se registraron ventas")

    submit = Button(top_window, bg="black", fg="white", text="Cargar datos", command=validate_date)
    submit.pack(pady=(5,0))           
                  


        
def not_sold_vehicles():

    top = new_window("Mostrar Vehículos No Vendidos")
    columns = ('vehiculo_codigo', 'vehiculo_marca', 'vehiculo_modelo', 'vehiculo_anio', 'vehiculo_km', 'vehiculo_precio', 'vehiculo_estatus')
    tree = ttk.Treeview(top, columns=columns, show='headings')

    tree.heading('vehiculo_codigo', text="Código")
    tree.heading('vehiculo_marca', text="Marca")
    tree.heading('vehiculo_modelo', text="Modelo")
    tree.heading('vehiculo_anio', text="Año")
    tree.heading('vehiculo_km', text="Kilometraje")
    tree.heading('vehiculo_precio', text='Precio')
    tree.heading('vehiculo_estatus', text='Estado')
    column_widths = (100, 100, 150, 80, 100, 120, 80)

    for i, column in enumerate(columns):
        tree.column(column, width=column_widths[i])
        tree.heading(column, text=column)

    read_vehicles()
    for x in range(0, len(vehiculo_codigo)):
        if vehiculo_estatus[x]=="0":
            tree.insert('', END, values=(vehiculo_codigo[x], vehiculo_marca[x], vehiculo_modelo[x], vehiculo_anio[x],
                                        vehiculo_km[x], (vehiculo_precio[x][0:6] + "," + vehiculo_precio[x][6:]),
                                        vehiculo_estatus[x]))

    tree.column(columns[-1], stretch=YES)
    tree.pack(fill=BOTH, expand=YES)  

def most_and_least_sold_vehicles():
    top = new_window("Vehículos más y menos vendidos")
    label = Label(top, text="Lista de vehículos más vendidos", justify="left", font=('Arial',20), bg="#000b1c", fg="#d9dadb")
    label.pack(pady=(5,15))
    columns = ('Modelo', 'Cantidad vendida')
    tree = ttk.Treeview(top, columns=columns, show='headings')
    tree.heading('Modelo', text='Modelo')
    tree.heading('Cantidad vendida', text='Cantidad Vendida')

    read_vehicles()
    lista_modelos_vendidos=[]
    for x in range(0,len(vehiculo_codigo)):
        if vehiculo_estatus[x]=="1":
            lista_modelos_vendidos.append(vehiculo_modelo[x])
    
    diccionario_modelos = {}

    for x in lista_modelos_vendidos:
        if x in diccionario_modelos:
            diccionario_modelos[x] = diccionario_modelos[x]+1
        else:
            diccionario_modelos[x] = 1
    
    diccionario_ordenado = sorted(diccionario_modelos.items(), key=lambda x: x[1], reverse=True)

    for modelo, conteo, in diccionario_ordenado:
        tree.insert('', END, values=(modelo, conteo))

    tree.pack()
        

        


#Se crea la ventana en tkinter, con un titulo, y el estado zoomed, que garantiza que se ejecute la ventana maximizada
ctypes.windll.shcore.SetProcessDpiAwareness(1)
window = Tk()
window.title('Sin Carros No Hay Paraíso')
window.state('zoomed')
window.tk.call('tk','scaling',1)


#Se declara la variable menu_bar, como un menú de tkinter, y luego se establece ese menú como el menu de la ventana
menu_bar = Menu(window)
menu_bar.config(bg="#000b1c")
window.config(menu=menu_bar, bg="#000b1c")


# ----- MENú PRINCIPAL -----
#se declara la variable menu como el menú de la ventana (tearoff=false es un parámetro que deshabilita un separador 
#en la primera posición del menú, el cual se utiliza para separar el menú hacia otra ventana)
menu = Menu(menu_bar, tearoff=False, bg="#000b1c", fg="#d9dadb")

#Se establece un submenú para vehículos con sus comandos, al final se agrega un cascade al menú principal, el cascade es un menú con subniveles
vehicle_submenu = Menu(menu, tearoff=False ,bg="#000b1c", fg="#d9dadb" )
vehicle_submenu.add_command(label='Mostrar Vehículos', command=show_vehicles  )
vehicle_submenu.add_command(label='Agregar Vehículos', command=add_vehicle)
menu.add_cascade(label='Vehículos', menu=vehicle_submenu )


#Submenú para ventas
sales_submenu = Menu(menu, tearoff=False ,bg="#000b1c", fg="#d9dadb" )
sales_submenu.add_command(label='Mostrar Ventas', command=show_sales )
sales_submenu.add_command(label='Agregar Ventas', command=add_sale )
menu.add_cascade(label = 'Ventas', menu=sales_submenu  )

#Se agrega un separador en el menú, para mostrar una opción de salir, que termine el programa
menu.add_separator()
menu.add_command(label='Salir', command=window.destroy)

#Se agrega el menu_bar como un cascade el menú principal
menu_bar.add_cascade(label="Menú", menu=menu)
# -------------------------------------------------------------------------

# ----- MENÚ DE ESTADÍSTICAS -----
#Se declara un nuevo menú para las estadísticas
stats_menu = Menu(menu_bar, tearoff=False ,bg="#000b1c", fg="#d9dadb" )

#Se agregan los comandos necesarios y un cascade para agregarlos al menú principal
stats_menu.add_command(label='Mostrar ventas por fecha', command=sale_by_date)
stats_menu.add_command(label='Mostrar vehículos sin vender', command=not_sold_vehicles)
stats_menu.add_command(label='Mostrar vehículo más y menos vendido', command=most_and_least_sold_vehicles)
menu_bar.add_cascade(label="Estadísticas y Registros", menu=stats_menu)
# ---------------------------------------------------------------------------------


label0 = Label(text='Bienvenido al concesionario, sin carros no hay paraiso!', justify='left', font=("Arial", 25), bg="#000b1c", fg="#d9dadb")
label0.pack(pady=(200, 1))

label1 = Label(text='Descripción del sistema: ', justify='left',pady=30, font=("Arial", 16, 'bold'),bg="#000b1c", fg="#d9dadb" )
label1.pack()

text= '''
En este sistema se tienen las siguientes funcionalidades:
• En el módulo de Vehículos se pueden agregar registros a nuestro catálogo, y consultar todos los vehículos registrados
• En el módulo de Clientes se pueden mostrar los clientes registrados en nuestro sistema
• En el módulo Ventas se pueden consultar todas las ventas realizadas, y agregar ventas, las ventas se pueden registrar a nombre de un cliente nuevo u otro ya existente
• En el apartado de estadísticas se permite mostrar elementos como los vehículos más vendidos, las ventas por fechas, y los vehículos sin vender
'''

label2 = Label(text=text,pady=5, font=("Arial", 14), justify='left', bg="#000b1c", fg="#d9dadb")
label2.pack()

label3 = Label(text="Utilice la barra de menús para navegar", pady=5,  font=("Arial", 14, "bold"), justify='left', bg="#000b1c", fg="#d9dadb")
label3.pack()

#Ejecución de la ventana principal
if __name__ == "__main__":
    window.mainloop() 