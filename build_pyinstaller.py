# pyinstaller로 exe파일 패키징하기 
'''build.bat >> pyinstaller depList.py --onefile'''



def my_function_1(func_arg1, func_arg2) :
    # ...<구현하고자 하는 기능 구현>...
    pass

def my_function_2(func_arg1, func_arg2) :
    # ...<구현하고자 하는 기능 구현>...
    pass


##################################################
def subcmd_aug_execute(args) :
    param1 = args.param1
    param2 = args.param2
    # ...
    my_function_1(param1, param2, ...)
    pass


def subcmd_aug_execute(args) :
    param1 = args.param1
    param2 = args.param2
    # ...
    my_function_2(param1, param2, ...)
    pass


##################################################
def add_subcmd_parser_do1(subparsers) :
    parser = subparsers.add_parser('do1', help="function 1")
    parser.add_argument("--param1", help="explain param1", required=Ture, type=str)
    parser.add_argument("--param2", help="explain param2", required=Ture, type=str)
    # ...
    parser.set_defaults(func=subcmd_do1_execute)
    return parser 

def add_subcmd_parser_do2(subparsers) :
    parser = subparsers.add_parser('do2', help="function 2")
    parser.add_argument("--param1", help="explain param1", required=Ture, type=str)
    parser.add_argument("--param2", help="explain param2", required=Ture, type=str)
    # ...
    parser.set_defaults(func=subcmd_do2_execute)
    return parser


##################################################
if __name__ == "__main__" :
    import argparse
    parser = argparse.ArgumentParser(prog='...')
    parser.add_argument('--version', action='version', version='1.0.1')
    subparsers = parser.add_subparsers(help='sub-commands for <app name 지정;comparing_tool>')

    parser1 = add_subcmd_parser_do1(subparsers)
    parser2 = add_subcmd_parser_do2(subparsers)

    if len(sys.argv) < 2 : 
        parser.print_help()
    elif "do1" == sys.argv[1] : 
        if len(sys.argv) < 3 : parser1.print_help()
        else : 
            args = parser.parse_args()
            args.func(args)
    elif "do2" == sys.argv[1] :
        if len(sys.argv) < 3 : parser2.print_help()
        else : 
            args = parser.parse_args() 
            args.func(args) 
