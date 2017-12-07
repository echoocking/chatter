write_file = '/Users/echoocking/anaconda/envs/MLPY3/lib/python3.5/site-packages/chatterbot_corpus/data/chinese/conversations.yml'
file_name = '/Users/echoocking/Downloads/xiaohuangji50w_nofenci.conv'
cp_file = '/Users/echoocking/anaconda/envs/MLPY3/lib/python3.5/site-packages/chatterbot_corpus/data/chinese/cp.yml'


def get_rid_of_unhealth_start_with(line):
    unhealth_start_with = [',','，','.', '?','<', '>', ':',';', '\"','\"', '\'', '{' ,'}', '~', '`','!','@','#', '$', '%', '^','&','*','(',')','-','+','=','|','[',']']
    for start_with in unhealth_start_with:
        if line.startswith(start_with):

            return '不要啦'

    return line


def gen_sentence():
    with open(file_name, 'r') as f:
        is_question = True
        for line in f:
            if line.startswith('E'):
                continue
            if line.startswith('M'):
                if is_question:
                    is_question = False
                    change_line = get_rid_of_unhealth_start_with(line.replace('M ', '').strip())

                    yield '- - '+change_line.strip()+'\n'
                    continue

                if not is_question:
                    is_question = True

                    change_line = get_rid_of_unhealth_start_with(line.replace('M ', '').strip())

                    yield '  - '+change_line.strip()+'\n'
                    continue


def write():
    with open(write_file, 'a+') as wf:
        sentens = gen_sentence()
        for line in sentens:
            wf.write(line)


def cut_file(num, rf, wf):
    with open(wf, 'a+') as wf:
        with open(rf, 'r') as rf:
            now_line_num = 1
            for line in rf:
                if now_line_num <= num:
                    wf.write(line)
                    now_line_num += 1
                else:
                    return

cut_file(20000, write_file, cp_file)


