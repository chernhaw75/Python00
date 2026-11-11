# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchern-h <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/11 11:16:52 by tchern-h          #+#    #+#              #
#    Updated: 2026/11/11 11:25:43 by tchern-h         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
	days = int(input("Days until harvest: "));
	count_down = 1;
	while (days+1 > count_down):
		print (f"Day {count_down}")
		count_down = count_down+1
	print("Harvest time!");
ft_count_harvest_iterative()

