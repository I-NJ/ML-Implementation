def findDecision(obj): #obj[0]: outlook, obj[1]: temperature, obj[2]: humidity, obj[3]: wind
	# {"feature": "outlook", "instances": 14, "metric_value": 0.3714, "depth": 1}
	if obj[0] == 'sunny':
		# {"feature": "humidity", "instances": 5, "metric_value": 0.0, "depth": 2}
		if obj[2] == 'high':
			return 'no '
		elif obj[2] == 'normal':
			return 'yes '
		else: return 'yes '
	elif obj[0] == 'rain':
		# {"feature": "wind", "instances": 5, "metric_value": 0.2, "depth": 2}
		if obj[3] == 'weak':
			return 'yes '
		elif obj[3] == 'strong':
			# {"feature": "temperature", "instances": 2, "metric_value": 0.0, "depth": 3}
			if obj[1] == 'cool':
				return 'no '
			elif obj[1] == 'mild':
				return 'no'
			else: return 'no'
		else: return 'no '
	elif obj[0] == 'overcast':
		return 'yes '
	else: return 'yes '
