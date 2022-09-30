'''
Author: Matayay Karuna
File Name: gamestopdb.py
Date Finished: 12/7/2021
'''



# Imports

import csv



# Functions

def menu( prompt, valid ):

    #Gives the user options on what they want to do.

    loop = True

    while loop:

        choice = input( prompt ).upper()

        if choice in ( valid ):

            loop = False

        else:

            print( "\nThat is not a valid response. Please try again." )

    return choice


def csvI( dbase ): 
        
    #Imports the gamestopdb.csv file to be used.

    with open( "./gamestopdb.csv" ) as game_stop:    
            
        records = csv.reader( game_stop )

        header = next( records )
            
        for record in records: 
               
            dbase.append( record )

    game_stop.close()

    return( dbase, header )


def csvW( dbase, heading ):

    #Rewrites the csv file for appending, deleting, and editing.

    game_stop = open( "./gamestopdb.csv", "w" )

    data = ""

    for a in range( 0, len( heading ) ):

        data += heading[a] + "," 
        
    data = data[:-1] + "\n"  
    game_stop.write( data )

    for i in range( 0, len( dbase ) ):

        data = ""

        for k in range( 0, len( dbase[i] ) ): 
                
            data += dbase[i][k] + "," 
                
        data = data[:-1] + "\n"  
        game_stop.write( data )
    
    game_stop.close()
    
    return


def totalT( data, heading ):

    #Displays all data in coloumns.

    underlines = "_"*150

    f_heading0 = f"{heading[0]:<40s}"
    f_heading1 = f"{heading[1]:<60s}"
    f_heading2 = f"{heading[2]:>20s}"
    f_heading3 = f"{heading[3]:>15s}"
    f_heading4 = f"{heading[4]:>10s}"

    print( "\n", f_heading0, f_heading1, f_heading2, f_heading3, f_heading4 )
    
    print( "\n", underlines , "\n", sep="" )
        
    for i in range( 0, len( data ) ):

        f_game = f"{data[i][0]:<40s}"
        f_platform = f"{data[i][1]:<60s}"
        f_price = f"{data[i][2]:>20s}"
        f_quantity = f"{data[i][3]:>15s}"
        f_cost = f"{data[i][4]:>10s}"
        
        print( f_game, f_platform, f_price, f_quantity, f_cost )

    return


def searchS( data, heading ):

    #Displays specific search in columns.

    game = input( "\nEnter the name of the game you would like to retrieve data on: " ).title()

    count = 0

    for i in range( 0, len( data ) ):

        try:

            test = data[count].index( game )

        except ValueError:

            count += 1

    underlines = "_"*150

    f_heading0 = f"{heading[0]:<40s}"
    f_heading1 = f"{heading[1]:<60s}"
    f_heading2 = f"{heading[2]:>20s}"
    f_heading3 = f"{heading[3]:>15s}"
    f_heading4 = f"{heading[4]:>10s}"

    print( "\n", f_heading0, f_heading1, f_heading2, f_heading3, f_heading4 )
    
    print( "\n", underlines , "\n", sep="" )

    f_search0 = f"{data[count][0]:<40s}"
    f_search1 = f"{data[count][1]:<60s}"
    f_search2 = f"{data[count][2]:>20s}"
    f_search3 = f"{data[count][3]:>15s}"
    f_search4 = f"{data[count][4]:>10s}"

    print( f_search0, f_search1, f_search2, f_search3, f_search4 )

    return count


def addA():

    #Adds a list to the list of lists database and gives the option to update the csv file.

    new_entry = []

    game = input( "\nEnter the name of the game you would like to add: " ).title()
    new_entry.append( game )

    platform = input( "\nEnter the platforms of this game: " ).title()
    new_entry.append( platform )

    price = input( "\nEnter the price of this game: " )
    new_entry.append( price )

    quantity = input( "\nEnter the amount of games in stock: " ) 
    new_entry.append( quantity )

    cost = input( "\nEnter the cost of the game: " )
    new_entry.append( cost )

    return new_entry


def deleteD( data ):

    #Deletes a list from the list of lists database and gives the option to update the csv file.

    delete_game = input( "\nEnter the name of the game you would like to delete: " ).title()

    count = 0

    for i in range( 0, len( data ) ):

        try:

            test = data[count].index( delete_game )

        except ValueError:

            count += 1

    game = data[count]

    return game


def editE():

    #Allows the editing of a specific quality on a specific game.

    pick_edit = input( "\nChoose what you want to edit. P - platform, M - price, Q - quantity, C - cost: " ).upper()

    if pick_edit in "P":

        edit = input( "\nEnter platforms: " )
        num = 1

    elif pick_edit in "M":

        edit = input( "\nEnter your price change: " )
        num = 2

    elif pick_edit in "Q":

        edit = input( "\nEnter your stock edit: " )
        num = 3

    elif pick_edit in "C":

        edit = input( "\nEnter the cost change: " )
        num = 4

    return( edit, num )


def revenueR( data ):

    #Calculates total potential revenue.

    all_rev = []

    for i in range( 0, len( data ) ):

        rev = data[i][2]
        rev = float( rev )
        
        all_rev.append( rev )

    t_rev_game = sum( all_rev )

    all_stock = []

    for j in range( 0, len( data ) ):

        stock = data[i][3]
        stock = int( stock )

        all_stock.append( stock )

    t_stock = sum( all_stock )

    t_rev = t_rev_game * t_stock

    return t_rev


def costC( data ):

    #Calculates total cost.

    all_cost = []

    for i in range( 0, len( data ) ):

        cost = data[i][4]
        cost = float( cost )
        
        all_cost.append( cost )

    t_cost_game = sum( all_cost )

    all_stock = []

    for j in range( 0, len( data ) ):

        stock = data[i][3]
        stock = int( stock )

        all_stock.append( stock )

    t_stock = sum( all_stock )

    t_cost = t_cost_game * t_stock

    return t_cost


def profitP( totalR, totalC ):

    #Calculates total potential profits.

    t_profit = totalR - totalC

    return t_profit



# Main Program

user_prompt = "\n\n\nI - import csv. T - view all data. S - view data for a specific game. \
A - add a game. D - delete a game. E - edit existing data. R - calculate total potential revenue. \
C - calculate total cost. P - calculate total potential profits. (PRESS Q TO QUIT). "

validity = [ "I", "T", "S", "A", "D", "E", "R", "C", "P", "Q" ]

loop = True
first_time = True

while loop:

    while first_time:

        user_menu = menu( user_prompt, validity )

        if user_menu in "Q":

            loop = False
            first_time = False
            print( "\nGoodbye" )

        elif user_menu in "I":

            main_dbase = []
            csv_main = csvI( main_dbase )

            #print( csv_main )

            print( "\nYou have imported your csv file." )

            first_time = False

        else:

            print( "\nThis is your first time running the program. You must import your csv file before performing other actions." )
    
    if user_menu not in "Q":

        user_menu = menu( user_prompt, validity )

        if user_menu in "Q":

            loop = False
            print( "\nGoodbye" )

        elif user_menu in "I":

            main_dbase = []
            csv_main = csvI( main_dbase )

            #print( csv_main )

            print( "\nYou have imported your csv file." )

        elif user_menu in "A":

            add_main = addA()

            decision = True
            
            while decision:

                update_file = input( "\nWould you like to add this information to your csv data file? Yes/No: " ).lower()

                if update_file in ( "yes", "no" ):

                    decision = False

                else:

                    print( "\nThat is an invalid response. Please try again." )

            if update_file in "yes":

                csv_main[0].append( add_main )
                add_data = csvW( csv_main[0], csv_main[1] )

                print( "\nYou have updated your csv file." )

            else:

                csv_main[0].append( add_main )

                print( "\nYou have not updated your csv file. If you import you csv file again your new entry will be lost." )

        elif user_menu in "T":

            display_all = totalT( csv_main[0], csv_main[1] )

        elif user_menu in "S":

            search_game = searchS( csv_main[0], csv_main[1] )

        elif user_menu in "D":

            delete_data = deleteD( csv_main[0] )

            perma_delete = True

            while perma_delete:

                file_delete = input( "\nWould you like to delete this information on your csv data file? Yes/No: " ).lower()

                if file_delete in ( "yes", "no" ):

                    perma_delete = False

                else:

                    print( "\nThat is an invalid response. Please try again." )

            if file_delete in "yes":

                csv_main[0].remove( delete_data )
                delete = csvW( csv_main[0], csv_main[1] )

                print( "\nYou have deleted your game from the csv file." )

            else:

                csv_main[0].remove( delete_data )

                print( "\nYou have deleted the data from your current program but not your csv file." )

        elif user_menu in "E":

            search_game = searchS( csv_main[0], csv_main[1] )

            edit_main = editE()

            perma_edit = True

            while perma_edit:

                file_edit = input( "\nWould you like to edit this information on your csv data file? Yes/No: " ).lower()

                if file_edit in ( "yes", "no" ):

                    perma_edit = False

                else:

                    print( "\nThat is an invalid response. Please try again." )

            if file_edit in "yes":

                pos = edit_main[1]

                del_pos = csv_main[0][search_game][pos]

                csv_main[0][search_game].insert( edit_main[1], edit_main[0] )
                csv_main[0][search_game].remove( del_pos )

                edit = csvW( csv_main[0], csv_main[1] )

                print( "\nYou have edited your game data." )

            else:

                pos = edit_main[1]

                del_pos = csv_main[0][search_game][pos]

                csv_main[0][search_game].insert( edit_main[1], edit_main[0] )
                csv_main[0][search_game].remove( del_pos )

                print( "\nYou have edited the data in your current program but not your csv file." )

        elif user_menu in "R":

            total_revenue = revenueR( csv_main[0] )
            
            print( "\n", "$", total_revenue, sep="" )

        elif user_menu in "C":

            total_cost = costC( csv_main[0] )

            print( "\n", "$", total_cost, sep="" )

        elif user_menu in "P":

            total_revenue = revenueR( csv_main[0] )
            total_cost = costC( csv_main[0] )

            total_profit = profitP( total_revenue, total_cost )

            print( "\n", "$", total_profit, sep="" )