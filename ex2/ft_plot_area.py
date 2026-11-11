# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchern-h <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/11 10:34:24 by tchern-h          #+#    #+#              #
#    Updated: 2026/11/11 11:01:48 by tchern-h         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():	
	length = input("Enter length: ")
	width = input("Enter width: ")
	area = int(length) * int(width);

	print(f"Plot area: {area}")
