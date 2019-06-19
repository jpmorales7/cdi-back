# from database import db
import datetime
from marshmallow import Schema, fields, pre_load, validate, post_load
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from models.Models import *

ma = Marshmallow()


class RoleSchema(ma.Schema):
    id = fields.Integer()
    userId = fields.Integer(attribute='userId', required=True)
    permits = fields.Integer(attribute='permits', required=True)

    @post_load
    def make_object(self, data):
        return Role(**data)


role_schema = RoleSchema()


class SonidosDeCosasYAnimalesSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer()
    am = fields.Boolean()
    ay = fields.Boolean()
    bee_mee = fields.Boolean()
    cuaCua = fields.Boolean()
    guauGuau_baBau = fields.Boolean()
    miau = fields.Boolean()
    muu = fields.Boolean()
    pio_pio = fields.Boolean()
    pum = fields.Boolean()
    qui_qui_ri_qui = fields.Boolean()
    rum_rum = fields.Boolean()
    tu_tu = fields.Boolean()
    total = fields.Integer()

    class Meta:
        model = SonidosDeCosasYAnimales

    @post_load
    def make_object(self, data):
        return SonidosDeCosasYAnimales(**data)


sonidosDeCosasYAnimales_schema = SonidosDeCosasYAnimalesSchema()


class AnimalesDeVerdadYDeJugueteSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer()
    abeja = fields.Boolean()
    animal = fields.Boolean()
    arana = fields.Boolean()
    ardilla = fields.Boolean()
    ballena = fields.Boolean()
    bicho = fields.Boolean()
    burro = fields.Boolean()
    caballo = fields.Boolean()
    cebra = fields.Boolean()
    chancho = fields.Boolean()
    ciervo_bambi = fields.Boolean()
    cocodrilo = fields.Boolean()
    conejo = fields.Boolean()
    cucaracha = fields.Boolean()
    elefante = fields.Boolean()
    foca = fields.Boolean()
    gallina = fields.Boolean()
    gato = fields.Boolean()
    gusano = fields.Boolean()
    hipopotamo = fields.Boolean()
    hormiga = fields.Boolean()
    jirafa = fields.Boolean()
    lechuza = fields.Boolean()
    leon = fields.Boolean()
    lobo = fields.Boolean()
    mariposa = fields.Boolean()
    mono = fields.Boolean()
    mosca = fields.Boolean()
    mosquito = fields.Boolean()
    oso = fields.Boolean()
    oveja = fields.Boolean()
    pajaro = fields.Boolean()
    pato = fields.Boolean()
    pavo = fields.Boolean()
    perro = fields.Boolean()
    pescado_pez = fields.Boolean()
    pinguino = fields.Boolean()
    pollito = fields.Boolean()
    rana = fields.Boolean()
    raton_rata = fields.Boolean()
    sapo = fields.Boolean()
    tigre = fields.Boolean()
    tortuga = fields.Boolean()
    vaca = fields.Boolean()
    vibora = fields.Boolean()
    total = fields.Integer()

    class Meta:
        model = AnimalesDeVerdadYDeJuguete

    @post_load
    def make_object(self, data):
        return AnimalesDeVerdadYDeJuguete(**data)


animalesDeVerdadYDeJuguete_schema = AnimalesDeVerdadYDeJugueteSchema()


class VehiculosDeVerdadYDeJugueteSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    ambulancia = fields.Boolean(nullable=True)
    auto = fields.Boolean(nullable=True)
    autoPolicia = fields.Boolean(nullable=True)
    avion = fields.Boolean(nullable=True)
    barco = fields.Boolean(nullable=True)
    bicicleta_bici = fields.Boolean(nullable=True)
    camion = fields.Boolean(nullable=True)
    camionDeBomberos = fields.Boolean(nullable=True)
    cochecitoDeBebe = fields.Boolean(nullable=True)
    helicoptero = fields.Boolean(nullable=True)
    micro_colectivo = fields.Boolean(nullable=True)
    moto = fields.Boolean(nullable=True)
    tractor = fields.Boolean(nullable=True)
    tren = fields.Boolean(nullable=True)
    triciclo = fields.Boolean(nullable=True)
    taxi = fields.Boolean(nullable=True)

    class Meta:
        model = VehiculosDeVerdadYDeJuguete

    @post_load
    def make_object(self, data):
        return VehiculosDeVerdadYDeJuguete(**data)


vehiculosDeVerdadYDeJuguete_schema = VehiculosDeVerdadYDeJugueteSchema()


class AlimentosYBebidasSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    aceituna = fields.Boolean(nullable=True)
    agua = fields.Boolean(nullable=True)
    alfajor = fields.Boolean(nullable=True)
    arroz = fields.Boolean(nullable=True)
    atun = fields.Boolean(nullable=True)
    azucar = fields.Boolean(nullable=True)
    banana = fields.Boolean(nullable=True)
    cafe = fields.Boolean(nullable=True)
    calabaza = fields.Boolean(nullable=True)
    caramelo = fields.Boolean(nullable=True)
    carne = fields.Boolean(nullable=True)
    cereales = fields.Boolean(nullable=True)
    chicle = fields.Boolean(nullable=True)
    choclo = fields.Boolean(nullable=True)
    chocolatada = fields.Boolean(nullable=True)
    chocolate = fields.Boolean(nullable=True)
    chupetin = fields.Boolean(nullable=True)
    coca = fields.Boolean(nullable=True)
    comida_papa = fields.Boolean(nullable=True)
    dulce = fields.Boolean(nullable=True)
    durazno = fields.Boolean(nullable=True)
    empanada = fields.Boolean(nullable=True)
    fideos = fields.Boolean(nullable=True)
    frutilla = fields.Boolean(nullable=True)
    galletita = fields.Boolean(nullable=True)
    hamburguesa_paty = fields.Boolean(nullable=True)
    helado = fields.Boolean(nullable=True)
    hielo = fields.Boolean(nullable=True)
    huevo = fields.Boolean(nullable=True)
    jamon = fields.Boolean(nullable=True)
    jugo = fields.Boolean(nullable=True)
    leche = fields.Boolean(nullable=True)
    lentejas = fields.Boolean(nullable=True)
    licuado = fields.Boolean(nullable=True)
    limonada = fields.Boolean(nullable=True)
    mani = fields.Boolean(nullable=True)
    manteca = fields.Boolean(nullable=True)
    manzana = fields.Boolean(nullable=True)
    mate = fields.Boolean(nullable=True)
    melon = fields.Boolean(nullable=True)
    mermelada = fields.Boolean(nullable=True)
    milanesa = fields.Boolean(nullable=True)
    naranja = fields.Boolean(nullable=True)
    pan = fields.Boolean(nullable=True)
    papasFritas = fields.Boolean(nullable=True)
    papas = fields.Boolean(nullable=True)
    pescado = fields.Boolean(nullable=True)
    pizza = fields.Boolean(nullable=True)
    pochoclo = fields.Boolean(nullable=True)
    pollo = fields.Boolean(nullable=True)
    queso = fields.Boolean(nullable=True)
    sal = fields.Boolean(nullable=True)
    salchicha_pancho = fields.Boolean(nullable=True)
    salsa = fields.Boolean(nullable=True)
    sandia = fields.Boolean(nullable=True)
    soda_gaseosa = fields.Boolean(nullable=True)
    sopa = fields.Boolean(nullable=True)
    te = fields.Boolean(nullable=True)
    tomate = fields.Boolean(nullable=True)
    torta = fields.Boolean(nullable=True)
    tortilla = fields.Boolean(nullable=True)
    uvas = fields.Boolean(nullable=True)
    vainilla = fields.Boolean(nullable=True)
    yogurt = fields.Boolean(nullable=True)
    zanahoria = fields.Boolean(nullable=True)
    zapallo = fields.Boolean(nullable=True)

    class Meta:
        model = AlimentosYBebidas

    @post_load
    def make_object(self, data):
        return AlimentosYBebidas(**data)


alimentosYBebidas_schema = AlimentosYBebidasSchema()


class RopaYAccesoriosSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    anteojos_lentes = fields.Boolean(nullable=True)
    aros = fields.Boolean(nullable=True)
    babero = fields.Boolean(nullable=True)
    bombacha = fields.Boolean(nullable=True)
    botas = fields.Boolean(nullable=True)
    boton = fields.Boolean(nullable=True)
    bike = fields.Boolean(nullable=True)
    bufanda = fields.Boolean(nullable=True)
    buzo = fields.Boolean(nullable=True)
    calzoncillo = fields.Boolean(nullable=True)
    camisa = fields.Boolean(nullable=True)
    campera = fields.Boolean(nullable=True)
    cartera = fields.Boolean(nullable=True)
    cierre = fields.Boolean(nullable=True)
    collar = fields.Boolean(nullable=True)
    gorra_gorro = fields.Boolean(nullable=True)
    guantes = fields.Boolean(nullable=True)
    hebillla_gomita = fields.Boolean(nullable=True)
    malla = fields.Boolean(nullable=True)
    medias = fields.Boolean(nullable=True)
    mochila = fields.Boolean(nullable=True)
    ojotas = fields.Boolean(nullable=True)
    pantalon = fields.Boolean(nullable=True)
    panal = fields.Boolean(nullable=True)
    pijama = fields.Boolean(nullable=True)
    polera = fields.Boolean(nullable=True)
    pullover = fields.Boolean(nullable=True)
    remera = fields.Boolean(nullable=True)
    ropa = fields.Boolean(nullable=True)
    saco = fields.Boolean(nullable=True)
    shorts = fields.Boolean(nullable=True)
    sombrero = fields.Boolean(nullable=True)
    vestido = fields.Boolean(nullable=True)
    zapatilla = fields.Boolean(nullable=True)
    zapato = fields.Boolean(nullable=True)
    zapatilla = fields.Boolean(nullable=True)

    class Meta:
        model = RopaYAccesorios

    @post_load
    def make_object(self, data):
        return RopaYAccesorios(**data)


ropaYAccesorios_schema = RopaYAccesoriosSchema()


class PartesDelCuerpoSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(fields.Integer, nullable=True)
    barba = fields.Boolean(nullable=True)
    bigote = fields.Boolean(nullable=True)
    boca = fields.Boolean(nullable=True)
    brazo = fields.Boolean(nullable=True)
    cabeza = fields.Boolean(nullable=True)
    cachete = fields.Boolean(nullable=True)
    cara = fields.Boolean(nullable=True)
    cola_culo = fields.Boolean(nullable=True)
    dedo = fields.Boolean(nullable=True)
    dientes = fields.Boolean(nullable=True)
    garganta_cuello = fields.Boolean(nullable=True)
    hombro = fields.Boolean(nullable=True)
    labios = fields.Boolean(nullable=True)
    lengua = fields.Boolean(nullable=True)
    mano = fields.Boolean(nullable=True)
    nariz = fields.Boolean(nullable=True)
    ojos = fields.Boolean(nullable=True)
    ombligo_pupo = fields.Boolean(nullable=True)
    oreja = fields.Boolean(nullable=True)
    panza = fields.Boolean(nullable=True)
    pecho_teta = fields.Boolean(nullable=True)
    pelo = fields.Boolean(nullable=True)
    pene_pito = fields.Boolean(nullable=True)
    piernas = fields.Boolean(nullable=True)
    pies_patas = fields.Boolean(nullable=True)
    rodilla = fields.Boolean(nullable=True)
    unas = fields.Boolean(nullable=True)
    vagina = fields.Boolean(nullable=True)

    class Meta:
        model = PartesDelCuerpo

    @post_load
    def make_object(self, data):
        return PartesDelCuerpo(**data)


partesDelCuerpo_schema = PartesDelCuerpoSchema()


class JuguetesSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True, default=0)
    birome_lapicera = fields.Boolean(nullable=True)
    bolitas = fields.Boolean(nullable=True)
    burbujas = fields.Boolean(nullable=True)
    crayones = fields.Boolean(nullable=True)
    cubos = fields.Boolean(nullable=True)
    fibras = fields.Boolean(nullable=True)
    globo = fields.Boolean(nullable=True)
    hoja_papel = fields.Boolean(nullable=True)
    juguete_chiche = fields.Boolean(nullable=True)
    lapiz = fields.Boolean(nullable=True)
    libro_cuento = fields.Boolean(nullable=True)
    muneca = fields.Boolean(nullable=True)
    osito = fields.Boolean(nullable=True)
    patines = fields.Boolean(nullable=True)
    pelicula_peli = fields.Boolean(nullable=True)
    pelota = fields.Boolean(nullable=True)
    peluche = fields.Boolean(nullable=True)
    pinturitas = fields.Boolean(nullable=True)
    plastilina = fields.Boolean(nullable=True)
    tambor = fields.Boolean(nullable=True)

    class Meta:
        model = Juguetes

    @post_load
    def make_object(self, data):
        return Juguetes(**data)


juguetes_schema = JuguetesSchema()


class UtensillosDeLaCasaSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(fields.Integer, nullable=True)
    alfombra = fields.Boolean(nullable=True)
    almohada = fields.Boolean(nullable=True)
    balde = fields.Boolean(nullable=True)
    basura = fields.Boolean(nullable=True)
    bolsa_bolsita = fields.Boolean(nullable=True)
    botella = fields.Boolean(nullable=True)
    caja = fields.Boolean(nullable=True)
    camara = fields.Boolean(nullable=True)
    canasta = fields.Boolean(nullable=True)
    celular_celu = fields.Boolean(nullable=True)
    cepillo = fields.Boolean(nullable=True)
    cepilloDeDientes = fields.Boolean(nullable=True)
    champu = fields.Boolean(nullable=True)
    chupete = fields.Boolean(nullable=True)
    cigarrillos_puchos = fields.Boolean(nullable=True)
    clavos = fields.Boolean(nullable=True)
    cuadro = fields.Boolean(nullable=True)
    cuchara = fields.Boolean(nullable=True)
    cuchillo = fields.Boolean(nullable=True)
    diario = fields.Boolean(nullable=True)
    dinero_plata = fields.Boolean(nullable=True)
    escoba = fields.Boolean(nullable=True)
    espejo = fields.Boolean(nullable=True)
    fosforo = fields.Boolean(nullable=True)
    fotos = fields.Boolean(nullable=True)
    frazada = fields.Boolean(nullable=True)
    jabon = fields.Boolean(nullable=True)
    lampara = fields.Boolean(nullable=True)
    llave = fields.Boolean(nullable=True)
    luz = fields.Boolean(nullable=True)
    mamadera_meme = fields.Boolean(nullable=True)
    martillo = fields.Boolean(nullable=True)
    olla = fields.Boolean(nullable=True)
    panuelo = fields.Boolean(nullable=True)
    papel = fields.Boolean(nullable=True)
    pastaDeDientes = fields.Boolean(nullable=True)
    peine = fields.Boolean(nullable=True)
    pelela = fields.Boolean(nullable=True)
    plancha = fields.Boolean(nullable=True)
    plato = fields.Boolean(nullable=True)
    reloj = fields.Boolean(nullable=True)
    remedio = fields.Boolean(nullable=True)
    servilleta = fields.Boolean(nullable=True)
    tachoDeBasura = fields.Boolean(nullable=True)
    taza = fields.Boolean(nullable=True)
    telefono = fields.Boolean(nullable=True)
    tenedor = fields.Boolean(nullable=True)
    tijeras = fields.Boolean(nullable=True)
    toalla = fields.Boolean(nullable=True)
    trapo = fields.Boolean(nullable=True)
    vaso = fields.Boolean(nullable=True)
    vela = fields.Boolean(nullable=True)

    class Meta:
        model = UtensillosDeLaCasa

    @post_load
    def make_object(self, data):
        return UtensillosDeLaCasa(**data)


utensillosDeLaCasa_schema = UtensillosDeLaCasaSchema()


class MueblesYCuartosSchema(ma.Schema):
    id = fields.Integer(primary_key=True)
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    banco = fields.Boolean(nullable=True)
    banadera = fields.Boolean(nullable=True)
    bano = fields.Boolean(nullable=True)
    bibloteca = fields.Boolean(nullable=True)
    cajon = fields.Boolean(nullable=True)
    cama = fields.Boolean(nullable=True)
    cochera_garage = fields.Boolean(nullable=True)
    cocina = fields.Boolean(nullable=True)
    computadora_compu = fields.Boolean(nullable=True)
    cuna = fields.Boolean(nullable=True)
    ducha = fields.Boolean(nullable=True)
    escaleras = fields.Boolean(nullable=True)
    estufa = fields.Boolean(nullable=True)
    habitacion_pieza = fields.Boolean(nullable=True)
    heladera = fields.Boolean(nullable=True)
    horno = fields.Boolean(nullable=True)
    inodoro = fields.Boolean(nullable=True)
    mesa = fields.Boolean(nullable=True)
    mueble = fields.Boolean(nullable=True)
    patio = fields.Boolean(nullable=True)
    piletaDeLavarManos = fields.Boolean(nullable=True)
    piso = fields.Boolean(nullable=True)
    placard = fields.Boolean(nullable=True)
    puerta = fields.Boolean(nullable=True)
    silla = fields.Boolean(nullable=True)
    sillon = fields.Boolean(nullable=True)
    television_tele = fields.Boolean(nullable=True)
    ventana = fields.Boolean(nullable=True)

    class Meta:
        model = MueblesYCuartos

    @post_load
    def make_object(self, data):
        return MueblesYCuartos(**data)


mueblesYCuartos_schema = MueblesYCuartosSchema()


class ObjetosFueraDeLaCasaSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    arbol = fields.Boolean(nullable=True)
    arena = fields.Boolean(nullable=True)
    bandera = fields.Boolean(nullable=True)
    cielo = fields.Boolean(nullable=True)
    cucha = fields.Boolean(nullable=True)
    estrella = fields.Boolean(nullable=True)
    flor = fields.Boolean(nullable=True)
    fuego = fields.Boolean(nullable=True)
    hamaca = fields.Boolean(nullable=True)
    hojas = fields.Boolean(nullable=True)
    humo = fields.Boolean(nullable=True)
    lluvia = fields.Boolean(nullable=True)
    luna = fields.Boolean(nullable=True)
    maceta = fields.Boolean(nullable=True)
    manguera = fields.Boolean(nullable=True)
    nieve = fields.Boolean(nullable=True)
    nube = fields.Boolean(nullable=True)
    pala = fields.Boolean(nullable=True)
    palo = fields.Boolean(nullable=True)
    pasto = fields.Boolean(nullable=True)
    piedra = fields.Boolean(nullable=True)
    piletaNatacion_pile = fields.Boolean(nullable=True)
    planta = fields.Boolean(nullable=True)
    reja = fields.Boolean(nullable=True)
    sol = fields.Boolean(nullable=True)
    techo = fields.Boolean(nullable=True)
    tierra_barro = fields.Boolean(nullable=True)
    timbre = fields.Boolean(nullable=True)
    tobogan = fields.Boolean(nullable=True)
    viento_aire = fields.Boolean(nullable=True)

    class Meta:
        model = ObjetosFueraDeLaCasa

    @post_load
    def make_object(self, data):
        return ObjetosFueraDeLaCasa(**data)


objetosFueraDeLaCasa_schema = ObjetosFueraDeLaCasaSchema()


class LugaresFueraDeLaCasaSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    banco = fields.Boolean(nullable=True)
    bosque = fields.Boolean(nullable=True)
    calesita = fields.Boolean(nullable=True)
    calle = fields.Boolean(nullable=True)
    campo = fields.Boolean(nullable=True)
    casa = fields.Boolean(nullable=True)
    cerro_montana = fields.Boolean(nullable=True)
    circo = fields.Boolean(nullable=True)
    cumpleanos_cumple = fields.Boolean(nullable=True)
    escuela_cole = fields.Boolean(nullable=True)
    fiesta = fields.Boolean(nullable=True)
    hospital_clinica = fields.Boolean(nullable=True)
    iglesia_templo = fields.Boolean(nullable=True)
    jardin = fields.Boolean(nullable=True)
    mar = fields.Boolean(nullable=True)
    pelotero = fields.Boolean(nullable=True)
    playa = fields.Boolean(nullable=True)
    plaza = fields.Boolean(nullable=True)
    rio = fields.Boolean(nullable=True)
    supermercado_super = fields.Boolean(nullable=True)
    vereda = fields.Boolean(nullable=True)
    zoologico = fields.Boolean(nullable=True)

    class Meta:
        model = LugaresFueraDeLaCasa

    @post_load
    def make_object(self, data):
        return LugaresFueraDeLaCasa(**data)


lugaresFueraDeLaCasa_schema = LugaresFueraDeLaCasaSchema()


class PersonasSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    abuela = fields.Boolean(nullable=True)
    abuelo = fields.Boolean(nullable=True)
    amiga = fields.Boolean(nullable=True)
    amigo = fields.Boolean(nullable=True)
    bebe = fields.Boolean(nullable=True)
    doctor = fields.Boolean(nullable=True)
    familia = fields.Boolean(nullable=True)
    hermana = fields.Boolean(nullable=True)
    hermano = fields.Boolean(nullable=True)
    madrina = fields.Boolean(nullable=True)
    maestra_seno = fields.Boolean(nullable=True)
    mama_mami = fields.Boolean(nullable=True)
    nina_nena = fields.Boolean(nullable=True)
    ninera = fields.Boolean(nullable=True)
    nino_nene = fields.Boolean(nullable=True)
    padrino = fields.Boolean(nullable=True)
    papa_papi = fields.Boolean(nullable=True)
    payaso = fields.Boolean(nullable=True)
    policia = fields.Boolean(nullable=True)
    prima = fields.Boolean(nullable=True)
    primo = fields.Boolean(nullable=True)
    senor = fields.Boolean(nullable=True)
    senora = fields.Boolean(nullable=True)
    policia = fields.Boolean(nullable=True)
    tia = fields.Boolean(nullable=True)
    tio = fields.Boolean(nullable=True)
    nombreDelInfante = fields.Boolean(nullable=True)

    class Meta:
        model = Personas

    @post_load
    def make_object(self, data):
        return Personas(**data)


personas_schema = PersonasSchema()


class RutinasReglasSocialesYJuegosSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    aVer_aPasear = fields.Boolean(nullable=True)
    adios_chau = fields.Boolean(nullable=True)
    ahiVoy = fields.Boolean(nullable=True)
    alAguaPatos = fields.Boolean(nullable=True)
    arribaLasManos = fields.Boolean(nullable=True)
    basta = fields.Boolean(nullable=True)
    besitos = fields.Boolean(nullable=True)
    buenasNoches = fields.Boolean(nullable=True)
    buenosDias = fields.Boolean(nullable=True)
    chasChas = fields.Boolean(nullable=True)
    cosquillita = fields.Boolean(nullable=True)
    cuco_acaEsta = fields.Boolean(nullable=True)
    dale = fields.Boolean(nullable=True)
    gol = fields.Boolean(nullable=True)
    gracias = fields.Boolean(nullable=True)
    hola = fields.Boolean(nullable=True)
    ojitos = fields.Boolean(nullable=True)
    perdon = fields.Boolean(nullable=True)
    pis = fields.Boolean(nullable=True)
    porFavor_porfi = fields.Boolean(nullable=True)
    pumba = fields.Boolean(nullable=True)
    queLindaManita = fields.Boolean(nullable=True)
    salud_chinChin = fields.Boolean(nullable=True)
    shhh = fields.Boolean(nullable=True)
    siesta_noniNoni = fields.Boolean(nullable=True)
    tortitas = fields.Boolean(nullable=True)
    unoDosTres = fields.Boolean(nullable=True)
    salud_chinChin = fields.Boolean(nullable=True)
    upa = fields.Boolean(nullable=True)
    vamos = fields.Boolean(nullable=True)
    vivaViva = fields.Boolean(nullable=True)
    yaEsta_listo = fields.Boolean(nullable=True)

    class Meta:
        model = RutinasReglasSocialesYJuegos

    @post_load
    def make_object(self, data):
        return RutinasReglasSocialesYJuegos(**data)


rutinasReglasSocialesYJuegos_schema = RutinasReglasSocialesYJuegosSchema()


class AccionesYProcesosSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    abrir = fields.Boolean(nullable=True)
    acabar = fields.Boolean(nullable=True)
    acompanar = fields.Boolean(nullable=True)
    acostar = fields.Boolean(nullable=True)
    agarrar = fields.Boolean(nullable=True)
    almorzar = fields.Boolean(nullable=True)
    andar = fields.Boolean(nullable=True)
    apagar = fields.Boolean(nullable=True)
    apurar = fields.Boolean(nullable=True)
    arreglar = fields.Boolean(nullable=True)
    asustar = fields.Boolean(nullable=True)
    atar = fields.Boolean(nullable=True)
    ayudar = fields.Boolean(nullable=True)
    bailar = fields.Boolean(nullable=True)
    bajar = fields.Boolean(nullable=True)
    banar = fields.Boolean(nullable=True)
    barrer = fields.Boolean(nullable=True)
    besar = fields.Boolean(nullable=True)
    buscar = fields.Boolean(nullable=True)
    caer = fields.Boolean(nullable=True)
    callar = fields.Boolean(nullable=True)
    caminar = fields.Boolean(nullable=True)
    cantar = fields.Boolean(nullable=True)
    cenar = fields.Boolean(nullable=True)
    cerrar = fields.Boolean(nullable=True)
    chupar = fields.Boolean(nullable=True)
    cocinar = fields.Boolean(nullable=True)
    comer = fields.Boolean(nullable=True)
    comprar = fields.Boolean(nullable=True)
    correr = fields.Boolean(nullable=True)
    cortar = fields.Boolean(nullable=True)
    dar = fields.Boolean(nullable=True)
    decir = fields.Boolean(nullable=True)
    dejar = fields.Boolean(nullable=True)
    desayunar = fields.Boolean(nullable=True)
    dibujar = fields.Boolean(nullable=True)
    doler = fields.Boolean(nullable=True)
    dormir = fields.Boolean(nullable=True)
    empujar = fields.Boolean(nullable=True)
    encontrar = fields.Boolean(nullable=True)
    ensenar = fields.Boolean(nullable=True)
    entrar = fields.Boolean(nullable=True)
    equivocar = fields.Boolean(nullable=True)
    esconder = fields.Boolean(nullable=True)
    escribir = fields.Boolean(nullable=True)
    escuchar = fields.Boolean(nullable=True)
    esperar = fields.Boolean(nullable=True)
    ganar = fields.Boolean(nullable=True)
    gritar = fields.Boolean(nullable=True)
    guardar = fields.Boolean(nullable=True)
    gustar = fields.Boolean(nullable=True)
    hablar = fields.Boolean(nullable=True)
    hacer = fields.Boolean(nullable=True)
    hamacar = fields.Boolean(nullable=True)
    ir = fields.Boolean(nullable=True)
    jugar = fields.Boolean(nullable=True)
    juntar = fields.Boolean(nullable=True)
    lastimar = fields.Boolean(nullable=True)
    lavar = fields.Boolean(nullable=True)
    leer = fields.Boolean(nullable=True)
    levantarse = fields.Boolean(nullable=True)
    llevar = fields.Boolean(nullable=True)
    llorar = fields.Boolean(nullable=True)
    meter = fields.Boolean(nullable=True)
    mirar = fields.Boolean(nullable=True)
    morder = fields.Boolean(nullable=True)
    mostrar = fields.Boolean(nullable=True)
    mover = fields.Boolean(nullable=True)
    nadar = fields.Boolean(nullable=True)
    oir = fields.Boolean(nullable=True)
    parar = fields.Boolean(nullable=True)
    patear = fields.Boolean(nullable=True)
    patinar = fields.Boolean(nullable=True)
    pegar = fields.Boolean(nullable=True)
    peinar = fields.Boolean(nullable=True)
    pensar = fields.Boolean(nullable=True)
    perder = fields.Boolean(nullable=True)
    pintar = fields.Boolean(nullable=True)
    poder = fields.Boolean(nullable=True)
    poner = fields.Boolean(nullable=True)
    prender = fields.Boolean(nullable=True)
    prestar = fields.Boolean(nullable=True)
    quedarse = fields.Boolean(nullable=True)
    quemarse = fields.Boolean(nullable=True)
    querer = fields.Boolean(nullable=True)
    quitar = fields.Boolean(nullable=True)
    regalar = fields.Boolean(nullable=True)
    respirar = fields.Boolean(nullable=True)
    romper = fields.Boolean(nullable=True)
    saber = fields.Boolean(nullable=True)
    sacar = fields.Boolean(nullable=True)
    salir = fields.Boolean(nullable=True)
    saltar = fields.Boolean(nullable=True)
    saludar = fields.Boolean(nullable=True)
    sentar = fields.Boolean(nullable=True)
    soplar = fields.Boolean(nullable=True)
    subir = fields.Boolean(nullable=True)
    tapar = fields.Boolean(nullable=True)
    tener = fields.Boolean(nullable=True)
    terminar = fields.Boolean(nullable=True)
    tirar = fields.Boolean(nullable=True)
    tocar = fields.Boolean(nullable=True)
    tomar = fields.Boolean(nullable=True)
    traer = fields.Boolean(nullable=True)
    venir = fields.Boolean(nullable=True)
    ver = fields.Boolean(nullable=True)
    volar = fields.Boolean(nullable=True)

    class Meta:
        model = AccionesYProcesos

    @post_load
    def make_object(self, data):
        return AccionesYProcesos(**data)


accionesYProcesos_schema = AccionesYProcesosSchema()


class EstadosSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    ser = fields.Integer(nullable=True)
    estar = fields.Integer(nullable=True)
    haber_hay = fields.Integer(nullable=True)

    class Meta:
        model = Estados

    @post_load
    def make_object(self, data):
        return Estados(**data)


estados_schema = EstadosSchema()


class CualidadesYAtributosSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    alto = fields.Boolean(nullable=True)
    amarillo = fields.Boolean(nullable=True)
    asco_asqueroso = fields.Boolean(nullable=True)
    azul = fields.Boolean(nullable=True)
    blanco = fields.Boolean(nullable=True)
    bueno = fields.Boolean(nullable=True)
    caca_popo = fields.Boolean(nullable=True)
    caliente = fields.Boolean(nullable=True)
    cansado = fields.Boolean(nullable=True)
    chico_chiquitito = fields.Boolean(nullable=True)
    despierto = fields.Boolean(nullable=True)
    diferente_distinto = fields.Boolean(nullable=True)
    dificil = fields.Boolean(nullable=True)
    duro = fields.Boolean(nullable=True)
    enfermo = fields.Boolean(nullable=True)
    enojado = fields.Boolean(nullable=True)
    feliz = fields.Boolean(nullable=True)
    feo = fields.Boolean(nullable=True)
    frio = fields.Boolean(nullable=True)
    fuerte = fields.Boolean(nullable=True)
    gordo = fields.Boolean(nullable=True)
    grande = fields.Boolean(nullable=True)
    hambre = fields.Boolean(nullable=True)
    igual = fields.Boolean(nullable=True)
    largo = fields.Boolean(nullable=True)
    lento = fields.Boolean(nullable=True)
    limpio = fields.Boolean(nullable=True)
    lindo = fields.Boolean(nullable=True)
    loco = fields.Boolean(nullable=True)
    lleno = fields.Boolean(nullable=True)
    malo = fields.Boolean(nullable=True)
    mejor = fields.Boolean(nullable=True)
    mentiroso = fields.Boolean(nullable=True)
    miedo_susto = fields.Boolean(nullable=True)
    mojado = fields.Boolean(nullable=True)
    mugriento = fields.Boolean(nullable=True)
    negro = fields.Boolean(nullable=True)
    nuevo = fields.Boolean(nullable=True)
    oscuro = fields.Boolean(nullable=True)
    peligroso = fields.Boolean(nullable=True)
    pesado = fields.Boolean(nullable=True)
    pobre = fields.Boolean(nullable=True)
    primero = fields.Boolean(nullable=True)
    rapido = fields.Boolean(nullable=True)
    rico = fields.Boolean(nullable=True)
    rojo = fields.Boolean(nullable=True)
    rosa = fields.Boolean(nullable=True)
    roto = fields.Boolean(nullable=True)
    ruidoso = fields.Boolean(nullable=True)
    seco = fields.Boolean(nullable=True)
    solo = fields.Boolean(nullable=True)
    suave = fields.Boolean(nullable=True)
    sucio = fields.Boolean(nullable=True)
    tranquilo = fields.Boolean(nullable=True)
    tonto_bobo = fields.Boolean(nullable=True)
    triste = fields.Boolean(nullable=True)
    ultimo = fields.Boolean(nullable=True)
    vacio = fields.Boolean(nullable=True)
    verde = fields.Boolean(nullable=True)
    viejo = fields.Boolean(nullable=True)
    violeta = fields.Boolean(nullable=True)

    class Meta:
        model = CualidadesYAtributos

    @post_load
    def make_object(self, data):
        return CualidadesYAtributos(**data)


cualidadesYAtributos_schema = CualidadesYAtributosSchema()


class PalabrasSobreElTiempoSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    aLaManana = fields.Boolean(nullable=True)
    aLaNoche = fields.Boolean(nullable=True)
    aLaTarde = fields.Boolean(nullable=True)
    ahora = fields.Boolean(nullable=True)
    anos = fields.Boolean(nullable=True)
    ayer = fields.Boolean(nullable=True)
    despues = fields.Boolean(nullable=True)
    dia = fields.Boolean(nullable=True)
    hoy = fields.Boolean(nullable=True)
    manana = fields.Boolean(nullable=True)
    noche = fields.Boolean(nullable=True)

    class Meta:
        model = PalabrasSobreElTiempo

    @post_load
    def make_object(self, data):
        return PalabrasSobreElTiempo(**data)


palabrasSobreElTiempo_schema = PalabrasSobreElTiempoSchema()


class PronombresYModificadoresSchema(ma.Schema):
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    aquel = fields.Boolean(nullable=True)
    aquellos = fields.Boolean(nullable=True)
    aquella = fields.Boolean(nullable=True)
    aquellas = fields.Boolean(nullable=True)
    el = fields.Boolean(nullable=True)
    ellos = fields.Boolean(nullable=True)
    ella = fields.Boolean(nullable=True)
    ellas = fields.Boolean(nullable=True)
    esa = fields.Boolean(nullable=True)
    esas = fields.Boolean(nullable=True)
    ese = fields.Boolean(nullable=True)
    eso = fields.Boolean(nullable=True)
    esos = fields.Boolean(nullable=True)
    esta = fields.Boolean(nullable=True)
    estas = fields.Boolean(nullable=True)
    este = fields.Boolean(nullable=True)
    esto = fields.Boolean(nullable=True)
    estos = fields.Boolean(nullable=True)
    le = fields.Boolean(nullable=True)
    les = fields.Boolean(nullable=True)
    lo = fields.Boolean(nullable=True)
    me = fields.Boolean(nullable=True)
    mi = fields.Boolean(nullable=True)
    mia = fields.Boolean(nullable=True)
    mias = fields.Boolean(nullable=True)
    mio = fields.Boolean(nullable=True)
    mios = fields.Boolean(nullable=True)
    nosotros = fields.Boolean(nullable=True)
    nuestro = fields.Boolean(nullable=True)
    se = fields.Boolean(nullable=True)
    su = fields.Boolean(nullable=True)
    suya = fields.Boolean(nullable=True)
    suyas = fields.Boolean(nullable=True)
    suyo = fields.Boolean(nullable=True)
    suyos = fields.Boolean(nullable=True)
    te = fields.Boolean(nullable=True)
    tu = fields.Boolean(nullable=True)
    tuya = fields.Boolean(nullable=True)
    tuyas = fields.Boolean(nullable=True)
    tuyo = fields.Boolean(nullable=True)
    tuyos = fields.Boolean(nullable=True)
    vos = fields.Boolean(nullable=True)
    yo = fields.Boolean(nullable=True)

    class Meta:
        model = PronombresYModificadores

    @post_load
    def make_object(self, data):
        return PronombresYModificadores(**data)


pronombresYModificadores_schema = PronombresYModificadoresSchema()


class PreguntasSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    como = fields.Boolean(nullable=True)
    cual = fields.Boolean(nullable=True)
    cuando = fields.Boolean(nullable=True)
    donde = fields.Boolean(nullable=True)
    porQue = fields.Boolean(nullable=True)
    que = fields.Boolean(nullable=True)
    quien = fields.Boolean(nullable=True)

    class Meta:
        model = Preguntas

    @post_load
    def make_object(self, data):
        return Preguntas(**data)


preguntas_schema = PreguntasSchema()


class PreposicionesYArticulosSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    a_al = fields.Boolean(nullable=True)
    con = fields.Boolean(nullable=True)
    de_del = fields.Boolean(nullable=True)
    el = fields.Boolean(nullable=True)
    en = fields.Boolean(nullable=True)
    entre = fields.Boolean(nullable=True)
    la = fields.Boolean(nullable=True)
    las = fields.Boolean(nullable=True)
    los = fields.Boolean(nullable=True)
    para = fields.Boolean(nullable=True)
    pero = fields.Boolean(nullable=True)
    un = fields.Boolean(nullable=True)
    una = fields.Boolean(nullable=True)
    unas = fields.Boolean(nullable=True)
    unos = fields.Boolean(nullable=True)

    class Meta:
        model = PreposicionesYArticulos

    @post_load
    def make_object(self, data):
        return PreposicionesYArticulos(**data)


preposicionesYArticulos_schema = PreposicionesYArticulosSchema()


class CuantificadoresYAdverbiosSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    asi = fields.Boolean(nullable=True)
    bien = fields.Boolean(nullable=True)
    despacio = fields.Boolean(nullable=True)
    mal = fields.Boolean(nullable=True)
    mas = fields.Boolean(nullable=True)
    mucho = fields.Boolean(nullable=True)
    nada = fields.Boolean(nullable=True)
    no = fields.Boolean(nullable=True)
    noHay = fields.Boolean(nullable=True)
    otro_otraVez = fields.Boolean(nullable=True)
    poco_poquito = fields.Boolean(nullable=True)
    rapido = fields.Boolean(nullable=True)
    si = fields.Boolean(nullable=True)
    todavia = fields.Boolean(nullable=True)
    todo = fields.Boolean(nullable=True)
    ya = fields.Boolean(nullable=True)

    class Meta:
        model = CuantificadoresYAdverbios

    @post_load
    def make_object(self, data):
        return CuantificadoresYAdverbios(**data)


cuantificadoresYAdverbios_schema = CuantificadoresYAdverbiosSchema()


class LocativosSchema(ma.Schema):
    id = fields.Integer(db.Integer, primary_key=True)
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    abajo = fields.Boolean(nullable=True)
    aca = fields.Boolean(nullable=True)
    adelante = fields.Boolean(nullable=True)
    adentro = fields.Boolean(nullable=True)
    afuera = fields.Boolean(nullable=True)
    ahi = fields.Boolean(nullable=True)
    alla = fields.Boolean(nullable=True)
    alLado = fields.Boolean(nullable=True)
    aqui = fields.Boolean(nullable=True)
    arriba = fields.Boolean(nullable=True)
    atras = fields.Boolean(nullable=True)
    cerca = fields.Boolean(nullable=True)
    enfrente = fields.Boolean(nullable=True)
    lejos = fields.Boolean(nullable=True)

    class Meta:
        model = Locativos

    @post_load
    def make_object(self, data):
        return Locativos(**data)


locativos_schema = LocativosSchema()


class ConectivosSchema(ma.Schema):
    id = fields.Integer()
    sectionA = fields.Integer(nullable=False)
    total = fields.Integer(nullable=True)
    entonces = fields.Boolean(nullable=True)
    o = fields.Boolean(nullable=True)
    porque = fields.Boolean(nullable=True)
    que = fields.Boolean(nullable=True)
    si = fields.Boolean(nullable=True)
    sino = fields.Boolean(nullable=True)
    tambien = fields.Boolean(nullable=True)
    y = fields.Boolean(nullable=True)

    class Meta:
        model = Conectivos

    @post_load
    def make_object(self, data):
        return Conectivos(**data)


conectivos_schema = ConectivosSchema()


class AddressSchema(ma.Schema):
    id = fields.Integer()
    adressline = fields.String(attribute='adressline', required=False, allow_none=True)
    city = fields.String(attribute='city', required=False, allow_none=True)
    country = fields.String(attribute='country', required=False, allow_none=True)
    postalCode = fields.String(attribute='postalCode', required=False, allow_none=True)
    province = fields.String(attribute='province', required=False, allow_none=True)
    childrenId = fields.String(attribute='childrenId', required=False, allow_none=True)

    class Meta:
        model = Address

    @post_load
    def make_object(self, data):
        return Address(**data)


address_schema = AddressSchema()


class ResultsSchema(ma.Schema):
    id = fields.Integer()
    result = fields.Integer(nullable=True)
    gender = fields.Str(nullable=True)
    surveyId = fields.Integer(nullable=False)
    age = fields.Integer(nullable=True)

    class Meta:
        model = Results

    @post_load
    def make_object(self, data):
        return Results(**data)


results_schema = ResultsSchema()




# TODO hay que hacer cuando tengamos todos los schemas
class SectionASchema(ma.Schema):
    id = fields.Integer()
    surveyId = fields.Integer(attribute='surveyId', required=False, allow_none=True)
    accionesYProcesos = fields.Nested(AccionesYProcesosSchema, attribute='surveyId', required=False, allow_none=True)
    alimentosYBebidas = fields.Nested(AlimentosYBebidasSchema, attribute='surveyId', required=False, allow_none=True)
    animalesDeVerdadYDeJuguete = fields.Nested(AnimalesDeVerdadYDeJugueteSchema, attribute='surveyId', required=False,
                                               allow_none=True)
    Conectivos = fields.Nested(ConectivosSchema, attribute='surveyId', required=False, allow_none=True)
    CualidadesYAtributos = fields.Nested(CualidadesYAtributosSchema, ttribute='surveyId', required=False,
                                         allow_none=True)
    CuantificadoresYAdverbios = fields.Nested(CuantificadoresYAdverbiosSchema, attribute='surveyId', required=False,
                                              allow_none=True)
    estados = fields.Nested(EstadosSchema, attribute='surveyId', required=False, allow_none=True)
    juguetes = fields.Nested(JuguetesSchema, attribute='surveyId', required=False, allow_none=True)
    locativos = fields.Nested(LocativosSchema)
    lugaresFueraDeLaCasa = fields.Nested(LugaresFueraDeLaCasaSchema)
    MueblesYCuartos = fields.Nested(MueblesYCuartosSchema)
    ObjetosFueraDeLaCasa = fields.Nested(ObjetosFueraDeLaCasaSchema)
    palabrasSobreElTiempo = fields.Nested(PalabrasSobreElTiempoSchema)
    partesDelCuerpo = fields.Nested(PartesDelCuerpoSchema)
    personas = fields.Nested(PersonasSchema)
    preguntas = fields.Nested(PreguntasSchema)
    preposicionesYArticulos = fields.Nested(PreposicionesYArticulosSchema)
    pronombresYModificadores = fields.Nested(PronombresYModificadoresSchema)
    ropaYAccesorios = fields.Nested(RopaYAccesoriosSchema)
    rutinasReglasSocialesYJuegos = fields.Nested(RutinasReglasSocialesYJuegosSchema)
    SonidosDeCosasYAnimales = fields.Nested(SonidosDeCosasYAnimalesSchema)
    utensillosDeLaCasa = fields.Nested(UtensillosDeLaCasaSchema)
    vehiculosDeVerdadYDeJuguete = fields.Nested(VehiculosDeVerdadYDeJugueteSchema)

    class Meta:
        model = SectionA

    @post_load
    def make_object(self, data):
        return SectionA(**data)


sectionA_schema = SectionASchema()


#
# class ContextSchema(ma.Schema):
#     id = fields.Integer()
#     childrenQuantity = fields.String(attribute='surveyId', required=False , allow_none=True)
#     familyGroup = fields.String(attribute='familyGroup', required=False)
#     childKeeper = fields.String(attribute='childKeeper', required=False)
#     anotherChildKeeper = fields.String(attribute='anotherChildKeeper', required=False)
#     kinderGarten = fields.String(attribute='kinderGarten', required=False)
#     kinderGartenHoursPerDay = fields.String(attribute='kinderGartenHoursPerDay', required=False)
#     kinderGartenHoursPerWeek = fields.String(attribute='kinderGartenHoursPerWeek', required=False)
#     languanguesContact = fields.String(attribute='languanguesContact', required=False)
#     languangues = fields.String(attribute='languangues', required=False)
#     languanguesAge = fields.String(attribute='languanguesAge', required=False)
#     educationTutor1 = fields.String(attribute='educationTutor1', required=False)
#     ocupationTutor1 = fields.String(attribute='ocupationTutor1', required=False)
#     educationTutor2 = fields.String(attribute='educationTutor2', required=False)
#     ocupationTutor2 = fields.String(attribute='ocupationTutor2', required=False)
#     childrenId = fields.Integer(attribute='childrenId', required=False)
#
#     class Meta:
#         model = Context
#
#     @post_load
#     def make_object(self, data):
#         return Context(**data)
#
#
# context_schema = ContextSchema()


class SurveySchema(ma.Schema):
    id = fields.Boolean(fields.Integer, primary_key=True)
    finished = fields.Boolean(attribute='finished')
    creationDate = fields.DateTime(attribute='creationDate')
    childrenId = fields.Integer(attribute='childrenId')
    sectionA = fields.Nested(SectionASchema, attribute='sectionA', many=True, allow_none=True)
    results = fields.Nested(ResultsSchema, attribute='results', many=True, allow_none=True)
    name = fields.String(nullable=True)
    dni = fields.Integer()
    gender = fields.String()
    birthday = fields.Date()
    age = fields.Integer()
    total = fields.Integer()

    @post_load
    def make_object(self, data):
        return Survey(**data)

    class Meta:
        model = Survey

    @post_load
    def make_object(self, data):
        return Survey(**data)


survey_schema = SurveySchema()


class ChildrenSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(attribute='name', required=False, allow_none=True)
    # lastname = fields.String(attribute='lastname', required=False , allow_none=True)
    dni = fields.Integer(attribute='dni', required=False, allow_none=True)
    birthday = fields.Date(attribute='birthday', required=False, allow_none=True)
    gender = fields.String(attribute='gender', required=False, allow_none=True)
    nameTutor1 = fields.String(attribute='nameTutor1', required=False, allow_none=True)
    nameTutor2 = fields.String(attribute='nameTutor2', required=False, allow_none=True)

    birthOrder = fields.Integer(attribute='birthOrder', required=False, allow_none=True)
    premature = fields.Boolean(attribute='premature', required=False, allow_none=True)
    gestationWeeks = fields.Integer(attribute='gestationWeeks', required=False, allow_none=True)
    birthWeight = fields.Integer(attribute='birthWeight', required=False, allow_none=True)
    hearingDisease = fields.Boolean(attribute='hearingDisease', required=False, allow_none=True)
    descriptionDisease = fields.String(attribute='descriptionDisease', required=False, allow_none=True)
    birthPlaceTutor1 = fields.String(attribute='birthPlaceTutor1', required=False, allow_none=True)
    birthPlaceTutor2 = fields.String(attribute='birthPlaceTutor2', required=False, allow_none=True)

    childrenQuantity = fields.Integer(attribute="childrenQuantity", required=False, allow_none=True)
    familyGroup = fields.String(attribute='familyGroup', required=False, allow_none=True)
    childKeeper = fields.String(attribute='childKeeper', required=False, allow_none=True)
    anotherChildKeeper = fields.String(attribute='anotherChildKeeper', required=False, allow_none=True)
    kinderGarden = fields.Boolean(attribute='kinderGarden', required=False, allow_none=True)
    kinderGardenHoursPerDay = fields.Integer(attribute='kinderGardenHoursPerDay', required=False, allow_none=True)
    kinderGardenHoursPerWeek = fields.Integer(attribute='kinderGardenHoursPerWeek', required=False, allow_none=True)
    kinderGardenSince = fields.String(attribute='kinderGardenSince', required=False, allow_none=True)
    languangesContact = fields.Boolean(attribute='languangesContact', required=False, allow_none=True)
    languanges = fields.String(attribute='languanges', required=False, allow_none=True)
    languangesAge = fields.Integer(attribute='languangesAge', required=False, allow_none=True)
    educationTutor1 = fields.String(attribute='educationTutor1', required=False, allow_none=True)
    ocupationTutor1 = fields.String(attribute='ocupationTutor1', required=False, allow_none=True)
    educationTutor2 = fields.String(attribute='educationTutor2', required=False, allow_none=True)
    ocupationTutor2 = fields.String(attribute='ocupationTutor2', required=False, allow_none=True)

    anyDisease = fields.Boolean(required=False, allow_none=True)

    countHearingDisease = fields.Integer(required=False, allow_none=True)
    healthProblem = fields.Boolean(required=False, allow_none=True)
    descriptionHealthProblem = fields.String(required=False, allow_none=True)
    surveyAnswer = fields.String(required=False, allow_none=True)
    languangeSpeaker = fields.String(required=False, allow_none=True)
    age = fields.Integer(required=False, allow_none=True)
    birthPlace = fields.String(required=False, allow_none=True)
    userId = fields.Integer(required=False, allow_none=True)

    survey = fields.Nested(SurveySchema, attribute='survey', many=False, allow_none=True, required=False)
    address = fields.Nested(AddressSchema, attribute='address', many=False, allow_none=True, required=False)

    class Meta:
        model = Children

    @post_load
    def make_object(self, data):
        return Children(**data)


children_schema = ChildrenSchema()


class UserSchema(ma.Schema):
    id = fields.Integer()
    username = fields.String(attribute='username', required=True)
    secretWord = fields.String(attribute='secretWord', required=True)
    role = fields.Nested(RoleSchema, attribute='role', allow_none=True)

    children = fields.Nested(ChildrenSchema, attribute='children', allow_none=True, required=False)

    class Meta:
        model = User

    @post_load
    def make_object(self, data):
        return User(**data)


user_schema = UserSchema()



#
# class SixteenSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Sixteen
#
#     @post_load
#     def make_object(self, data):
#         return Sixteen(**data)
#
#
# sixteen_schema = SixteenSchema()
#
#
# class SeventeenSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Seventeen
#
#     @post_load
#     def make_object(self, data):
#         return Seventeen(**data)
#
#
# seventeen_schema = SeventeenSchema()
#
#
# class EighteenSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Eighteen
#
#     @post_load
#     def make_object(self, data):
#         return Eighteen(**data)
#
#
# eighteen_schema = EighteenSchema()
#
#
# class NineteenSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Nineteen
#
#     @post_load
#     def make_object(self, data):
#         return Nineteen(**data)
#
#
# nineteen_schema = NineteenSchema()
#
#
# class TwentySchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Twenty
#
#     @post_load
#     def make_object(self, data):
#         return Twenty(**data)
#
#
# twenty_schema = TwentySchema()
#
#
# class TwentyoneSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Twentyone
#
#     @post_load
#     def make_object(self, data):
#         return Twentyone(**data)
#
#
# twentyone_schema = TwentyoneSchema()
#
#
# class TwentytwoSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Twentytwo
#
#     @post_load
#     def make_object(self, data):
#         return Twentytwo(**data)
#
#
# twentytwo_schema = TwentytwoSchema()
#
#
# class TwentythreeSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Twentythree
#
#     @post_load
#     def make_object(self, data):
#         return Twentythree(**data)
#
#
# twentythree_schema = TwentythreeSchema()
#
#
# class TwentyfourSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Twentyfour
#
#     @post_load
#     def make_object(self, data):
#         return Twentyfour(**data)
#
#
# twentyfour_schema = TwentyfourSchema()
#
#
# class TwentyfiveSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Twentyfive
#
#     @post_load
#     def make_object(self, data):
#         return Twentyfive(**data)
#
#
# twentyfour_schema = TwentyfiveSchema()
#
#
# class TwentysixSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Twentysix
#
#     @post_load
#     def make_object(self, data):
#         return Twentysix(**data)
#
#
# twentysix_schema = TwentysixSchema()
#
#
# class TwentysevenSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Twentyseven
#
#     @post_load
#     def make_object(self, data):
#         return Twentyseven(**data)
#
#
# twentyseven_schema = TwentysevenSchema()
#
#
# class TwentyeightSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Twentyeight
#
#     @post_load
#     def make_object(self, data):
#         return Twentyeight(**data)
#
#
# twentyeight_schema = TwentyeightSchema()
#
#
# class TwentynineSchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Twentynine
#
#     @post_load
#     def make_object(self, data):
#         return Twentynine(**data)
#
#
# twentynine_schema = TwentynineSchema()
#
#
# class ThirtySchema(ma.Schema):
#     id = fields.Integer()
#     result = fields.Integer()
#     surveyId = fields.Integer()
#     gender = fields.String()
#
#     class Meta:
#         model = Thirty
#
#     @post_load
#     def make_object(self, data):
#         return Thirty(**data)
#
#
# thirty_schema = ThirtySchema()
