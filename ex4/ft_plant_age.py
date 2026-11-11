# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchern-h <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/11 10:52:34 by tchern-h          #+#    #+#              #
#    Updated: 2026/11/11 11:08:19 by tchern-h         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age_check():
	plant_age = int(input("Enter plant age in days: "))
	if (plant_age > 60):
		print("Plant ready to harvest")
	else:
		print("Plant need more time to grow")
