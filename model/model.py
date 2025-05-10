from database import corso_DAO, studente_DAO


class Model:
    def __init__(self):
        pass

    def getcorsi(self):
        #print(corso_DAO.get_corsi())
        return corso_DAO.get_corsi()

    def getIscrittiCorso(self, corso):
        return  corso_DAO.get_iscritti_corso(corso)

    def cerca_studente(self, matricola):
        return studente_DAO.cerca_studente(matricola)

    def get_corsi_studente(self, matricola):
        return corso_DAO.get_corsi_studente(matricola)

    def iscrivi_corso(self, matricola, codin):
        return corso_DAO.iscrivi_corso(matricola, codin)