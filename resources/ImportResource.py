import flask
from flask_restful import Resource
import logging

from models.Models import Children, db
from models.Schemas import ChildrenSchema


class ImportData(Resource):
    def post(self):
        data = flask.request.get_json(force=False, silent=True)
        logging.info('Payload: {}'.format(data))

        children = ChildrenSchema()

        children.name = data.get("NombreNino")
        children.gender = data.get("Sexo")
        children.dni = data.get()
        children.age = data.get("Edad")
        children.birthday = data.get("FechaNacimiento")
        children.birthPlace = data.get("Lugar_de_Nacimiento")
        children.gender = data.get("Genero")
        children.nameTutor1 = data.get("Madre_Nombre")
        children.nameTutor2 = data.get("Padre_Nombre")
        if data.get("Orden_de_nacimiento_del_nino_1_2_3") is not None:
            children.birthOrder = data.get("Orden_de_nacimiento_del_nino_1_2_3")
        else:
            children.birthOrder = data.get("Otro_especifique")

        children.premature = data.get("Nacio_antes_de_los_9_meses_si_no")
        children.gestationWeeks = data.get("Con_cuantas_semanas_de_gestacion")
        children.birthWeight = data.get("Peso_al_nacer")
        children.hearingDisease = data.get("Tuvo_infecciones_de_oido_si_no")
        children.descriptionDisease = data.get("Si_respondio_Si_Descripcion_del_problema_textual")
        children.birthPlaceTutor1 = data.get("Lugar_de_origen_M")
        children.birthPlaceTutor2 = data.get("Lugar_de_origen_P")

        children.childrenQuantity = data.get("Cuantos_ninos_hay_en_tu_familia")
        children.familyGroup = data.get("Quienes_viven_con_el_nino")
        children.childKeeper = data.get()
        children.anotherChildKeeper = data.get("ConQuienMayormente")

        children.kinderGarden = data.get("Tu_hijo_va_a_la_guarderia_si_no")
        children.kinderGardenHoursPerDay = data.get("Cuantas_horas_al_dia")
        children.kinderGardenHoursPerWeek = data.get("Cuantas_veces_por_semana")
        children.kinderGardenSince = data.get("DesdeCuandoGuarderia")
        children.languangesContact = data.get("ContactoOtrasLenguas")
        children.languanges = data.get("CualLengua")
        children.languangesAge = data.get("Desde_que_edad_en_meses")
        children.languangeSpeaker = data.get("Con_quien_o_quienes_la_habla")

        children.educationTutor1 = data.get("Escolaridad_Madre")
        children.ocupationTutor1 = data.get("Madre_Ocupacion")
        children.educationTutor2 = data.get("Escolaridad_Padre")
        children.ocupationTutor2 = data.get("Padre_ocupacion")
        children.anyDisease = data.get("Tuvo_alguna_enfermedad_o_problema_de_audicion_o_lenguaje_si_no")
        children.countHearingDisease = data.get("Si_respondio_Si_Cuantas_veces_por_ano")
        children.healthProblem = data.get("Problema_salud_antes_durante_despues")
        children.descriptionHealthProblem = data.get("Por_favor_describir_el_problema_textual")
        children.surveyAnswer = data.get("Quien_respondio")

        db.session.add(children)
        db.session.commit()
        # "Nombre_el_Nino","Sexo","FECHA_NACIMIENTO","FECHA_de_HOY","30/03/2018","Edad_en_Meses")
        # logging.info('Payload: {}'.format(surveyData))
