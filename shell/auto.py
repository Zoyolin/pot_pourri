#!/bin/python
import subprocess

tests = [
(" aaa/bbb/ccc/ddd/eee/fff","aaa/bbb/ccc/ddd/eee/fff"),
("",""),
("''","''"),
(".","."),
(" aaa","aaa"),
("/aaa","/aaa"),
("/aaa/","/aaa/"),
("/aaa/bbb","/aaa/bbb"),
("/aaa/bbb/","/aaa/bbb/"),
(" aaa/bbbb","aaa/bbbb"),
("/aaa/bbb/ccc/ddd/eee/fff","/aaa/bbb/ccc/ddd/eee/fff"),
(" a/b/f","a/b/f"),
(" Alligator/Braguette/filouterie","Alligator/Bra/filouterie"),
(" Alligator/Braguette/filouterie/hiu","Alligator/Bra/fil/hiu"),
(" Alligator/Braguette/filouterie/hiu/","Alligator/Bra/fil/hiu/"),
(" Alligator/Braguette/filouterie/hiu/jjj","Alligator/Bra/fil/hiu/jjj"),
(" Alligator/Braguette/filouterie/hiu/jjj/","Alligator/Bra/fil/hiu/jjj/"),
("`pwd`","`pwd`"),
("test","test"),
("/thisdoc","/thisdoc"),
("thisdoc","thisdoc"),
("thisdoc/","thisdoc/"),
("thisdoc//","thisdoc/"),
("/thisdoc/","/thi/"),
("/thisdoc","/thisdoc"),
("u//hhh","u/hhh"),
("u/hhh","u/hhh"),
("u/hhh/","u/hhh/"),
("u/hhh/kkk//","u/hhh/kkk/"),
("/U/kkkk/k/ss","/U/kkk/k/ss"),
("/U/kkkk/k/ss/","/U/kkk/k/ss/"),
("/U/kkkkk/ss/","/U/kkk/ss/"),
("/Ulor/kkkkwef/kwfgw/ss","/Ulo/kkk/kwf/ss"),
("Ulor/kkkkwef/kwfgw/ss","Ulor/kkk/kwf/ss"),
("/u/ss","/u/ss"),
("u/ss","u/ss"),
("/U/ss","/U/ss"),
("/U/ss/","/U/ss/"),
("y","y"),
("/yy","/yy"),
("/yy/","/yy/"),
("yy/","yy/"),
("/yy/jjj/kkk/","/yy/jjj/kkk/"),
("yy/jjj/kkk/","yy/jjj/kkk/"),
("yy/kkk/","yy/kkk/"),
("yyy/","yyy/"),
("yyy/HHH","yyy/HHH"),
("yyy/HHH/III","yyy/HHH/III"),
("yyy/HHH/III/","yyy/HHH/III/"),
("lorem/ipsum/dolor/sicmen/ditumb/huoir","lorem/ips/dol/sic/dit/huoir"),
("/lorem/ipsum/dolor/sicmen/ditumb/huoir","/lor/ips/dol/sic/dit/huoir"),
("/lorem/ipsum/dolor/sicmen/ditumb/huoir/","/lor/ips/dol/sic/dit/huo/"),
("lorem/ipsum/dolor/sicmen/ditumb/huoir/","lorem/ips/dol/sic/dit/huo/"),
("lorem/ipsum/dolor/#sicmen/ditumb/huoir","lorem/ips/dol/#si/dit/huoir"),]


def build():
    cmd = ["cmake", ".."]
    if subprocess.run(cmd):
        cmd = ["make"]
        subprocess.run(cmd)


def run(arg):
    cmd = ["./ps1_shortener.run", arg]
    res = subprocess.run(cmd, capture_output=True)
    return res.stdout.decode("utf-8")


def run_tests():
    for test in tests:
        result = run(test[0])
        assert result == test[1], f"in : {test[0]}, out : {result}, expect : {test[1]}"


def gen_tests():
    for test in tests:
        result = run(test[0])
        print(f'("{test[0]}","{result}"),')


build()
gen_tests()
