import argparse
import pickle
import os
from main_network import Network
from main_network import Topology
from main_network import Slice

# Function to save the data structure of the network contained in "obj" to file "file_name"
def save_object(obj, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(obj, file)
    print(f"Oggetto salvato come {file_name}")

# Function to load the data structure of the network stored in "file_name"
def load_object(file_name):
    with open(file_name, 'rb') as file:
        obj = pickle.load(file)
    print(f"Oggetto caricato da {file_name}")
    return obj

# Function for adding a network topology, which can be the main one or the one associated with a slice
def add(file_name, option, my_network):
    print(f"Eseguita add con opzione {option} e file {file_name}")
    # Se l'opzione è '-s', richiedi un ID numerico
    if option == '-s':
        slice_id = input("Inserisci un ID numerico: ")
        try:
            slice_id = int(slice_id)
            my_network.add_slice(file_name, option, slice_id)
        except ValueError:
            print("ID non valido. L'operazione 'add' non è stata completata.")
    else:
        my_network.add_topology(file_name)
    return

# Function for showing the entire network topology, the main one and the one or more associated with a slice
def show(my_network):
    my_network.print()

# Function to delete a network topology, if the network topology is the main one, all the slices will also be deleted.
def delete(file_name, option, my_network):
    print(f"delete con opzione {option} e file {file_name}")
    if option == '-t':   
        my_network.delete_topology(file_name)
    else:
        my_network.delete_slice(file_name)
    return

# Function for activating a slice
def activate(file_name, my_network):
    print(f"activate con file {file_name}")
    my_network.activate_slice(file_name)

# Function for deactivating a slice
def deactivate(file_name, my_network):
    print(f"deactivate con file {file_name}")
    my_network.deactivate_slice(file_name)

# Main function where the command line interface is defined
def main():
    my_network = Network()
    my_network = load_object('saved_object.pkl')

    parser = argparse.ArgumentParser(description='CLI application for on demand SDN slices in ComNetsEmu')
    parser.add_argument('operation', choices=['add', 'show', 'delete', 'activate','deactivate'],help='Select a main operation')
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-t', action='store_true', help='Option -t')
    group.add_argument('-s', action='store_true', help='Option -s')
    parser.add_argument('-f','--file', dest='file_name', help='Name of the text file')

    args = parser.parse_args()

    if args.operation in [ 'add' , 'delete' ]:
        if not args.t and not args.s:
            parser.error('You must specify one of the -t or -s options for operations <add> <delete>')
        elif not args.file_name:
            parser.error('You must specify a file name for operations <add> <delete>')
        else:
            if args.operation == 'add':
                add(args.file_name, '-t' if args.t else '-s', my_network)
            elif args.operation == 'delete':
                delete(args.file_name, '-t' if args.t else '-s', my_network)
    else:
        if args.operation == 'activate':
            activate(args.file_name, my_network)
        elif args.operation == 'deactivate':
            deactivate(args.file_name, my_network)
        elif args.operation == 'show':
            show(my_network)

    save_object(my_network, 'saved_object.pkl')

if __name__ == "__main__":
    main()




