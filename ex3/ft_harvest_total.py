# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchern-h <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/11 10:46:58 by tchern-h          #+#    #+#              #
#    Updated: 2026/11/11 11:00:30 by tchern-h         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	day1 = input("Day 1 harvest: ")
	day2 = input("Day 2 harvest: ")
	day3 = input("Day 3 harvest: ")
	total = int(day1) + int(day2) + int(day3)

	print(f"Total harvest: {total}");
