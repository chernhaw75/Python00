# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchern-h <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/11 12:51:54 by tchern-h          #+#    #+#              #
#    Updated: 2026/11/11 12:53:20 by tchern-h         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
	seed_type_cap = seed_type[:1].upper() + seed_type[1:]
	if unit == "area":
		print(f"{seed_type_cap}: {quantity} square meters")
	elif unit == "grams":
		print(f"{seed_type_cap}: {quantity} grams total")
	elif unit == "packets":
		print(f"{seed_type_cap}: {quantity} packets avaliable")
	else:
		print("Unknown unit type")

