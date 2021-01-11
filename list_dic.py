#!/usr/bin/env python3

List = [['张玉琦', 'P279-1', 'CYP79-GANRAO-F'], ['张玉琦', 'P279-1', 'CYP79-GANRAO-R'], ['张玉琦', 'P249-1', 'CYP49-GANRAO-F'], ['张玉琦', 'P249-1', 'CYP49-GANRAO-R'], ['张玉琦', 'P271-1', 'CYP71-GANRAO-F'], ['张玉琦', 'P271-1', 'CYP71-GANRAO-R'], ['张玉琦', 'P257-1', 'CYP57-GANRAO-F'], ['张玉琦', 'P257-1', 'CYP57-GANRAO-R'], ['张玉琦', 'P2247-1', 'CYP247-GANRAO-F'], ['张玉琦', 'P2247-1', 'CYP247-GANRAO-R'], ['张玉琦', '194W1', 'CYP194-R'], ['张玉琦', '194W1', 'CYP194-F'], ['张玉琦', '194W2', 'CYP194-R'], ['张玉琦', '194W2', 'CYP194-F'], ['张玉琦', '194W3', 'CYP194-R'], ['张玉琦', '194W3', 'CYP194-F'], ['张玉琦', '194W4', 'CYP194-R'], ['张玉琦', '194W4', 'CYP194-F'], ['张玉琦', '194W5', 'CYP194-R'], ['张玉琦', '194W5', 'CYP194-F'], ['何聆瑜', '28A-8-4', '(Y3936)28A-8-4-W6R'], ['田宇', 'UBI78-6', '(Y3937)UBI78-4-W1F'], ['田宇', 'UBI78-5', '(Y3937)UBI78-4-W1F'], ['田宇', 'UBI78-4', '(Y3937)UBI78-4-W1F'], ['陈阳', '5-2', '(Y3938)5-2-W4F'], ['李永光', 'G10-CAS9-MD123-1', '(Y3939)G10-CAS9-MD123-1-W1F'], ['李永光', 'CAS9-MD123-2', '(Y3940)CAS9-MD123-2-W1F'], ['于忠洋', '1-2-5-2', '(Y3941)1-2-5-2-W1CF'], ['陈韵竹', 'J7-1-3', '(Y3942)J7-1-3-W1F']]


Dict = {}
List_tmp = []
for i in List:
    List_tmp += [i[0]]
Name = list(set(List_tmp))

print(Name)

for name in Name:
    # Adding names as first keys
    Dict.update({name:{}})
    Sample_tmp = []
    for i in List:
        if name == i[0]:
            Sample_tmp += [i[1]]
    Sample_tmp = list(set(Sample_tmp))
    # adding  smaple as second layer keys
    for sample in Sample_tmp:
        Dict[name].update({sample:{}})


for name in Dict.keys():

    for sample  in Dict[name].keys():
        primer_tmp = []
        for i in List:
            if name == i[0] and sample == i[1]:
                primer_tmp += [i[2]]
        Dict[name][sample] = primer_tmp




print(Dict)
