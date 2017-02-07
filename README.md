## RGSTR
NFC based registration system for schools

Year 13 A level project. 
v.1 Uses an NFC card to sign in and out of the database register.

# Libraries
-RGSTRadd
	
	Contains subroutines used to easily add users to the database from a file or individually.

-RGSTRconnect
	
	Contains functions for connecting to the database, including reading from the config file.

-RGSTRsetup
	
	Contains functions to set up the database tables if they are not found by the program.

-RGSTRupdate
	
	Used to lookup and change values in the database, for example if a card is scanned.

# Programs
-RGSTRControlPanel
	
	Used to manage the database, including queries, reports, adding users and importing from a file. Front end GUI for use by office staff, can be run from any computer connected to the network.

-RGSTRMain
	
	Used to scan cards and users in and out. Must be run on raspberry pi including EXPLORE-NFC board.
