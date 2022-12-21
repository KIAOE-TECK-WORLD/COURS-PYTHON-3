# Ecrire 3 Class
#
# Une classe Student
# 	params: name, level
#	functions:
#		_get_name(self)
#		_get_level(self)
#
#
# Une classe NoteSummary
# 	params: subject, note, student
# 	functions:
# 		_get_subject(self)
# 		_get_level(self)
# 		_get_student(self)
#
# 		_get_student_stack(self)
# 		# return < STUDENT_STACK >
# 		# Contrainte
# 			# définissez de manière globale la STACK
# 			# C'est ainsi que vous pourriez y avoir accès de manière globale
#			# Voir aussi utilisation du mot clé GLOBAL en PYTHON ( AIDE )
#
# 		# Exemple: STACK.get(<STUDENT_NAME>)
# 			Cette instruction récupère le dictionnaire dans la stack globale
# 			par la clé qui est le nom de l'étudiant.
# 			Voir Exemple du dictionnaire de _add_in_stack
#
# 		_add_in_stack(self)
# 			# add note to subject
# 			# {
# 				'<STUDENT_NAME>': {
#
# 					'subject1': note1,
# 					'subject2': note2,
# 					'subject3': note3,
# 					'subject4': note4,
# 					'subject5': note5,
# 					'subject6': note6,
#
# 				}
#
# 			  }
#
#
# Une classe CalcMoy
# 	params: note_summary, _moy, _mention
# 	functions:
# 		_get_moy(self)
# 			# Retourne la moyenne
#
# 		_get_mention(self)
# 			# Retourne la mention
# 			# if self._get_moy() >= 10
# 				# ADMIS
# 			# else ( self._get_moy < 10)
# 				# ECHOUE
#
# 		moy(self)
# 			# calcule la moyenne et la retourne
#