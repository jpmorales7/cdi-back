import logging

import flask

from flask_restful import Resource
from models.Schemas import *
from resources.ResourceHelper import resource_helper


class CreateSurvey(Resource):
    def post(self, user):
        data = flask.request.get_json(force=False, silent=True)

        logging.info('Payload: {}'.format(data))
        try:

            data = flask.request.get_json(force=False, silent=True)
            survey, errors = survey_schema.load(data)
            if errors:
                logging.error(errors)
                raise Exception(errors=errors)

            children = Children.query.filter_by(userId=user).first()

            survey.childrenId = children.id
            survey.creationDate = datetime.datetime.now()
            survey.finished = False
            db.session.add(survey)

            sectionA = SectionA()
            survey = Survey.query.filter_by(childrenId=children.id).first()
            sectionA.surveyId = survey.id
            db.session.add(sectionA)
            db.session.commit()
            msg = 'Survey: {} was created successfully'.format(survey.id)
            logging.info(msg)
            return resource_helper.response(msg, 201)
        except Exception as ex:
            msg_error = 'Error trying to create survey, msjError: {}'.format(ex)
            logging.error(msg_error)
            return resource_helper.response(msg_error, 400)


class UpdateSurvey(Resource):
    def post(self, table, user):
        data = flask.request.get_json(force=False, silent=True)
        dataAux = flask.request.get_json(force=False, silent=True)

        count = 0

        for key, value in dataAux.items():
            if value:
                count = count + 1
        try:

            children = Children.query.filter_by(userId=user).first()
            survey = Survey.query.filter_by(childrenId=children.id).first()
            sectionA = SectionA.query.filter_by(surveyId=survey.id).first()

            sw = Switcher()
            return_table, errors = sw.switch_table(table, data, sectionA.id)
            if errors:
                logging.error(errors)
                raise Exception(errors)

            return_table.sectionAId = sectionA.id

            return_table.total = count
            db.session.add(return_table)
            db.session.commit()
            msg = 'Table was created successfully'
            logging.info(msg)
            return resource_helper.response(msg, 201)
        except Exception as ex:
            msg_error = 'Error trying to create table, msjError: {}'.format(ex)
            logging.error(msg_error)
            return resource_helper.response(msg_error, 400)

    def put(self, table, user):
        data = flask.request.get_json(force=False, silent=True)
        dataAux = flask.request.get_json(force=False, silent=True)

        count = 0

        for key, value in dataAux.items():
            if value:
                count = count + 1
        try:
            children = Children.query.filter_by(userId=user).first()
            survey = Survey.query.filter_by(childrenId=children.id).first()
            sectionA = SectionA.query.filter_by(surveyId=survey.id).first()

            sw = Switcher()
            return_table, errors = sw.switch_table(table, data, sectionA.id)
            if errors:
                logging.error(errors)
                raise Exception(errors)

            return_table.total = count
            return_table.sectionAId = sectionA.id
            db.session.add(return_table)
            db.session.commit()

            survey.finished = True

            totalSurvey = self.getTotal(survey.id)
            survey.total = totalSurvey
            db.update(Survey).where(id == survey.id)
            results = self.results(survey.id, survey.gender, survey.total, survey.age)
            db.session.add(results)
            db.session.commit()
            msg = 'Finished survey {}'.format(survey.id)
            logging.info(msg)
            return resource_helper.response(msg, 201)

        except Exception as ex:
            msg_error = 'Error trying to create table, not finished survey. MsjError: {}'.format(ex)
            logging.error(msg_error)
            return resource_helper.response(msg_error, 400)

    def getTotal(self, surveyId):
        sectionA = SectionA.query.filter_by(surveyId=surveyId).first()

        surveyTotal = 0

        surveyTotal = surveyTotal + db.session().query(AnimalesDeVerdadYDeJuguete.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(AlimentosYBebidas.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(SonidosDeCosasYAnimales.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(RopaYAccesorios.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(PartesDelCuerpo.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(Juguetes.total).filter_by(sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(UtensillosDeLaCasa.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(MueblesYCuartos.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(ObjetosFueraDeLaCasa.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(LugaresFueraDeLaCasa.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(Personas.total).filter_by(sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(RutinasReglasSocialesYJuegos.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(AccionesYProcesos.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(Estados.total).filter_by(sectionAId=sectionA.id).first().total

        surveyTotal = surveyTotal + db.session().query(CuantificadoresYAdverbios.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(PalabrasSobreElTiempo.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(PronombresYModificadores.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(Preguntas.total).filter_by(sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(PreposicionesYArticulos.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(CuantificadoresYAdverbios.total).filter_by(
            sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(Locativos.total).filter_by(sectionAId=sectionA.id).first().total
        surveyTotal = surveyTotal + db.session().query(Conectivos.total).filter_by(sectionAId=sectionA.id).first().total

        return surveyTotal

    def results(self, surveyId, gender, total, age):
        results = Results()
        results.gender = gender
        results.surveyId = surveyId
        results.result = total
        results.age = age
        return results


class Switcher(object):
    def switch_table(self, tableId, json_data, sectionAId):
        func = getattr(self, tableId, "invalid table")
        return func(json_data, sectionAId)

    def sonidosDeCosasYAnimales(self, json_data, sectionAId):
        sonidosDeCosasYAnimales, errors = sonidosDeCosasYAnimales_schema.load(json_data)
        repetido = SonidosDeCosasYAnimales.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(SonidosDeCosasYAnimales).filter(SonidosDeCosasYAnimales.sectionAId == sectionAId).delete()
            db.session.commit()

        return sonidosDeCosasYAnimales, errors

    def animalesDeVerdadYDeJuguete(self, json_data, sectionAId):
        animalesDeVerdadYDeJuguete, errors = animalesDeVerdadYDeJuguete_schema.load(json_data)
        repetido = AnimalesDeVerdadYDeJuguete.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(AnimalesDeVerdadYDeJuguete).filter(
                AnimalesDeVerdadYDeJuguete.sectionAId == sectionAId).delete()
            db.session.commit()

        return animalesDeVerdadYDeJuguete, errors

    def vehiculosDeVerdadYDeJuguete(self, json_data, sectionAId):
        vehiculosDeVerdadYDeJuguete, errors = vehiculosDeVerdadYDeJuguete_schema.load(json_data)
        repetido = VehiculosDeVerdadYDeJuguete.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(VehiculosDeVerdadYDeJuguete).filter(
                VehiculosDeVerdadYDeJuguete.sectionAId == sectionAId).delete()
            db.session.commit()

        return vehiculosDeVerdadYDeJuguete, errors

    def alimentosYBebidas(self, json_data, sectionAId):
        alimentosYBebidas, errors = alimentosYBebidas_schema.load(json_data)
        repetido = AlimentosYBebidas.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(AlimentosYBebidas).filter(
                AlimentosYBebidas.sectionAId == sectionAId).delete()
            db.session.commit()
        return alimentosYBebidas, errors

    def ropaYAccesorios(self, json_data, sectionAId):
        ropaYAccesorios, errors = ropaYAccesorios_schema.load(json_data)
        repetido = RopaYAccesorios.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(RopaYAccesorios).filter(
                RopaYAccesorios.sectionAId == sectionAId).delete()
            db.session.commit()
        return ropaYAccesorios, errors

    def partesDelCuerpo(self, json_data, sectionAId):
        partesDelCuerpo, errors = partesDelCuerpo_schema.load(json_data)
        repetido = PartesDelCuerpo.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(PartesDelCuerpo).filter(
                PartesDelCuerpo.sectionAId == sectionAId).delete()
            db.session.commit()
        return partesDelCuerpo, errors

    def juguetes(self, json_data, sectionAId):
        juguetes, errors = juguetes_schema.load(json_data)
        repetido = Juguetes.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(Juguetes).filter(
                Juguetes.sectionAId == sectionAId).delete()
            db.session.commit()
        return juguetes, errors

    def utensillosDeLaCasa(self, json_data, sectionAId):
        utensillosDeLaCasa, errors = utensillosDeLaCasa_schema.load(json_data)
        repetido = UtensillosDeLaCasa.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(UtensillosDeLaCasa).filter(
                UtensillosDeLaCasa.sectionAId == sectionAId).delete()
            db.session.commit()
        return utensillosDeLaCasa, errors

    def mueblesYCuartos(self, json_data, sectionAId):
        mueblesYCuartos, errors = mueblesYCuartos_schema.load(json_data)
        repetido = MueblesYCuartos.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(MueblesYCuartos).filter(
                MueblesYCuartos.sectionAId == sectionAId).delete()
            db.session.commit()
        return mueblesYCuartos, errors

    def objetosFueraDeLaCasa(self, json_data, sectionAId):
        objetosFueraDeLaCasa, errors = objetosFueraDeLaCasa_schema.load(json_data)
        repetido = ObjetosFueraDeLaCasa.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(ObjetosFueraDeLaCasa).filter(
                ObjetosFueraDeLaCasa.sectionAId == sectionAId).delete()
            db.session.commit()
        return objetosFueraDeLaCasa, errors

    def lugaresFueraDeLaCasa(self, json_data, sectionAId):
        lugaresFueraDeLaCasa, errors = lugaresFueraDeLaCasa_schema.load(json_data)
        repetido = LugaresFueraDeLaCasa.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(LugaresFueraDeLaCasa).filter(
                LugaresFueraDeLaCasa.sectionAId == sectionAId).delete()
            db.session.commit()
        return lugaresFueraDeLaCasa, errors

    def personas(self, json_data, sectionAId):
        personas, errors = personas_schema.load(json_data)
        repetido = Personas.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(Personas).filter(
                Personas.sectionAId == sectionAId).delete()
            db.session.commit()
        return personas, errors

    def rutinasReglasSocialesYJuegos(self, json_data, sectionAId):
        rutinasReglasSocialesYJuegos, errors = rutinasReglasSocialesYJuegos_schema.load(json_data)
        repetido = RutinasReglasSocialesYJuegos.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(RutinasReglasSocialesYJuegos).filter(
                RutinasReglasSocialesYJuegos.sectionAId == sectionAId).delete()
            db.session.commit()

        return rutinasReglasSocialesYJuegos, errors

    def accionesYProcesos(self, json_data, sectionAId):
        accionesYProcesos, errors = accionesYProcesos_schema.load(json_data)
        repetido = AccionesYProcesos.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(AccionesYProcesos).filter(
                AccionesYProcesos.sectionAId == sectionAId).delete()
            db.session.commit()
        return accionesYProcesos, errors

    def estados(self, json_data, sectionAId):
        estados, errors = estados_schema.load(json_data)
        repetido = Estados.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(Estados).filter(Estados.sectionAId == sectionAId).delete()
            db.session.commit()

        return estados, errors

    def cualidadesYAtributos(self, json_data, sectionAId):
        cualidadesYAtributos, errors = cualidadesYAtributos_schema.load(json_data)
        repetido = CualidadesYAtributos.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(CualidadesYAtributos).filter(CualidadesYAtributos.sectionAId == sectionAId).delete()
            db.session.commit()
        return cualidadesYAtributos, errors

    def palabrasSobreElTiempo(self, json_data, sectionAId):
        palabrasSobreElTiempo, errors = palabrasSobreElTiempo_schema.load(json_data)
        repetido = PalabrasSobreElTiempo.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(PalabrasSobreElTiempo).filter(PalabrasSobreElTiempo.sectionAId == sectionAId).delete()
            db.session.commit()
        return palabrasSobreElTiempo, errors

    def pronombresYModificadores(self, json_data, sectionAId):
        pronombresYModificadores, errors = pronombresYModificadores_schema.load(json_data)
        repetido = PronombresYModificadores.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(PronombresYModificadores).filter(
                PronombresYModificadores.sectionAId == sectionAId).delete()
            db.session.commit()
        return pronombresYModificadores, errors

    def preguntas(self, json_data, sectionAId):
        preguntas, errors = preguntas_schema.load(json_data)
        repetido = Preguntas.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(Preguntas).filter(Preguntas.sectionAId == sectionAId).delete()
            db.session.commit()
        return preguntas, errors

    def preposicionesYArticulos(self, json_data, sectionAId):
        preposicionesYArticulos, errors = preposicionesYArticulos_schema.load(json_data)
        repetido = PreposicionesYArticulos.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(PreposicionesYArticulos).filter(PreposicionesYArticulos.sectionAId == sectionAId).delete()
            db.session.commit()
        return preposicionesYArticulos, errors

    def cuantificadoresYAdverbios(self, json_data, sectionAId):
        cuantificadoresYAdverbios, errors = cuantificadoresYAdverbios_schema.load(json_data)
        repetido = CuantificadoresYAdverbios.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(CuantificadoresYAdverbios).filter(
                CuantificadoresYAdverbios.sectionAId == sectionAId).delete()
            db.session.commit()
        return cuantificadoresYAdverbios, errors

    def locativos(self, json_data, sectionAId):
        locativos, errors = locativos_schema.load(json_data)
        repetido = Locativos.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(Locativos).filter(
                Locativos.sectionAId == sectionAId).delete()
            db.session.commit()
        return locativos, errors

    def conectivos(self, json_data, sectionAId):
        conectivos, errors = conectivos_schema.load(json_data)
        repetido = Conectivos.query.filter_by(sectionAId=sectionAId).first()
        if repetido is not None:
            db.session.query(Conectivos).filter(
                Conectivos.sectionAId == sectionAId).delete()
            db.session.commit()
        return conectivos, errors


class SurveyResource(Resource):
    def get(self, user):
        try:
            logging.info('getting survey from children {}'.format(user))
            children = Children.query.filter_by(userId=user).first()
            survey = Survey.query.filter_by(childrenId=children.id).first()
            if survey is not None:
                survey_dict = resource_helper.make_dict_survey(survey)
                return resource_helper.response(survey_dict, 200)
        except Exception as ex:
            msg_error = 'Error getting survey. MsjError: {}'.format(ex)
            logging.error(msg_error)
            return resource_helper.response(msg_error, 400)
