import json

from flask import Response


class ResourceHelper():

    def make_dic_user(self, user):
        role = None
        if user.role is not None:
            role = dict(
                permits=user.role.permits
            )
        children_dict = dict(
            id=user.id,
            username=user.username,
            secretWord=user.secretWord,
            role=role
        )
        return children_dict

    def response(self, response, status=201, mimetype='application/json'):
        result = Response(
            response=json.dumps(response),
            mimetype=mimetype,
            status=status
        )
        return result

    def make_dic_children(self, children):
        children_dict = dict(
            id=children.id,
            name=children.name,
            #    lastname=children.lastname,
            dni=children.dni,
            birthday=str(children.birthday),
            gender=children.gender,
            nameTutor1=children.nameTutor1,
            nameTutor2=children.nameTutor2,
            birthOrder=children.birthOrder,
            premature=children.premature,
            gestationWeeks=children.gestationWeeks,
            birthWeight=children.birthWeight,
            hearingDisease=children.hearingDisease,
            descriptionDisease=children.descriptionDisease,
            birthPlaceTutor1=children.birthPlaceTutor1,
            birthPlaceTutor2=children.birthPlaceTutor2,
            childrenQuantity=children.childrenQuantity,
            familyGroup=children.familyGroup,
            childKeeper=children.childKeeper,
            anotherChildKeeper=children.anotherChildKeeper,
            kinderGarden=children.kinderGarden,
            kinderGardenHoursPerDay=children.kinderGardenHoursPerDay,
            kinderGardenHoursPerWeek=children.kinderGardenHoursPerWeek,
            languangesContact=children.languangesContact,
            languanges=children.languanges,
            languangesAge=children.languangesAge,
            languangueSpeaker=children.languangeSpeaker,
            educationTutor1=children.educationTutor1,
            ocupationTutor1=children.ocupationTutor1,
            educationTutor2=children.educationTutor2,
            ocupationTutor2=children.ocupationTutor2,
            anyDisease=children.anyDisease,
            countHearingDisease=children.countHearingDisease,
            healthProblem=children.healthProblem,
            descriptionHealthProblem=children.descriptionHealthProblem,
            surveyAnswer=children.surveyAnswer,
            userId=children.userId
        )
        return children_dict

    def make_dict_survey(self, survey):
        survey_dic = dict(
            id=survey.id,
            creationDate=str(survey.creationDate),
            childrenId=survey.childrenId,
            finished=survey.finished,
            name=survey.name,
            dni=survey.dni,
            gender=survey.gender,
            birthday=str(survey.birthday),
            age=survey.age
        )
        return survey_dic


resource_helper = ResourceHelper()
