note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

print(notes)
print(note1)





moyenne_eleve1 = (note1[2]+note2[2]+note3[2]+note4[2]+note5[2]+note6[2])/6
print(moyenne_eleve1)

moyenne_mathseleve1 = (note1[2]+note3[2]+note6[2])/3
print(moyenne_mathseleve1)


def moyenne_tuples(notes, eleve, matiere):
  res = [item for item in notes if item[0]==eleve]
  res1 = [item for item in notes if item[1]==matiere]
  return sum([x[2] for x in res])/len(res)

print("La moyenne de l'élève 1 en math est : ", moyenne_tuples(notes, 'eleve1', 'math'))
print("La moyenne de l'élève 1 en physique est : ",moyenne_tuples(notes, 'eleve1', 'physique'))
print("La moyenne de l'élève 1 en économie est : ", moyenne_tuples(notes, 'eleve1', 'eco'))
print("La moyenne de l'élève 2 en math est : ", moyenne_tuples(notes, 'eleve2', 'math'))


class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur  

  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)

  # Question 6
  def __str__(self):
    return print(Note)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

# Question 5
onotes = []
for i in notes:
  onotes.append(Note(i[0], i[1], i[2]))
Note.afficher(onotes)


# Question 6
for x in range(len(onotes)):
  print(onotes[x])

# Question 7
notes_enregistrées = []
for k in range(len(notes_enregistrées)):
  print(notes_enregistrées[k])

# Question 8
def moyenne_Notes(nom_eleve = None, matiere = None):
  liste = notes_enregistrées
  res = []
  liste_eleves = []
  for x in liste :
    liste_eleves = [i for i in liste if i.eleve == nom_eleve or nom_eleve == None]
    liste_matieres = [i for i in liste_eleves if i.matiere == matiere or matiere == None]
    res = [i.valeur for i in liste_matieres]
    moyenne = sum(res)/len(res)
    return moyenne
print(moyenne_Notes())
  















  















