# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchern-h <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/11 11:27:58 by tchern-h          #+#    #+#              #
#    Updated: 2026/11/11 11:32:35 by tchern-h         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(days=None, current=1):
    if days is None:
        days = int(input("Days until harvest: "))
    if current > days:
        print("Harvest time!")
        return
    print(f"Day {current}")
    ft_count_harvest_recursive(days, current + 1)
	 
