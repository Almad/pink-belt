import argparse

import handle_trello

def trello_arguments(parent_parser, subparser):
    trello_parser = subparser.add_parser("t", help="Trello",                                                                                    
                    parents=[parent_parser])
    
    action_subparser = trello_parser.add_subparsers(title="action",                                                                                         
                     dest="action_command")                                                                                                               

    migrate_parser = action_subparser.add_parser("migrate-label", help="second",
                    parents=[parent_parser])

    for l in ['label', 'board', 'column', 'board-to', 'column-to']:
        migrate_parser.add_argument('--'+l, dest=l.replace('-', '_'))



def define_arguments():
    # parser = argparse.ArgumentParser(
    #     description='Manage Apiary like a boss',
    #     # prog='black-belt',
    #     add_help=False
    # )


    parent_parser = argparse.ArgumentParser(add_help=False)                                                                                                  
    # parent_parser.add_argument('--user', '-u',                                                                                                               
    #                     default=getpass.getuser(),                                                                                                           
    #                     help='username')                                                                                                                     
    # parent_parser.add_argument('--debug', default=False, required=False,                                                                                     
    #                            action='store_true', dest="debug", help='debug flag')                                                                         

    main_parser = argparse.ArgumentParser()                                                                                                                  
    
    service_subparsers = main_parser.add_subparsers(title="service",                                                                                         
                    dest="service_command")

    trello_arguments(parent_parser, service_subparsers)


    args = main_parser.parse_args()

    DISPATCH_MAP = {
        't' : handle_trello.dispatch_command
    }

    if args.service_command in DISPATCH_MAP:
        DISPATCH_MAP[args.service_command](args)
    else:
        raise Exception("%s not found in DISPATCH_MAP" % args.service_command)



def main():
    define_arguments()

